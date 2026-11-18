"""One-command bulk RMT Final local orchestration (Python 3.11+).

Preserves first-attempt API requests, source prompts, separate people, approved
Pass@1 results, and unapproved public-example smoke checks. No request is sent
without an interactive paid-usage confirmation.

Run: py run_all_final.py
Rerun if interrupted: successful/attempted prompts are skipped by runner_final.
"""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import getpass
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import zipfile

ROOT=Path(__file__).resolve().parent
PEOPLE=('person_1','person_2','person_3')
PAYLOAD='outputs'

sys.path.insert(0,str(ROOT))
import runner_final as runner

def stamp():
    return datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')

def preflight_count():
    all_tasks=[]
    for p in PEOPLE:
        doc,pending=runner.generate_pending(p)
        all_tasks.append((p,doc,pending))
        print(f'{p}: pending paid requests={len(pending)}, already preserved={90-len(pending)}, audited flags={sum(bool(t["audit_flags"]) for t in doc["tasks"])}',flush=True)
    return all_tasks

def run_cmd(cmd,logfile=None,timeout=None):
    print('>',' '.join(cmd),flush=True)
    cp=subprocess.run(cmd,cwd=ROOT,timeout=timeout)
    if cp.returncode !=0:
        print('WARNING: command failed with exit status',cp.returncode,'(saved evidence remains)',flush=True)
    return cp.returncode

def real_check():
    print('\n== Available approved regression suites ==',flush=True)
    approved=0
    for p in PEOPLE:
        doc=runner.person_data(p)
        approved+=sum(runner.test_ready(p,str(t['problem_id']))[0] for t in doc['tasks'])
    print(f'Approved task suites: {approved}/135. Unapproved examples are NOT valid Pass@1 evidence.')
    return approved

def generate_all(workers:int,max_paid:int):
    datasets=preflight_count()
    total=sum(len(pending) for _,_,pending in datasets)
    if not total:
        print('All prompts already generated or have preserved attempt logs; no paid requests needed.')
        return
    if total>max_paid:
        print(f'STOP: pending {total} requests exceeds --max-paid {max_paid}. Nothing charged. Use --max-paid {total} explicitly to proceed.')
        return
    print('\nATTENTION: You are about to issue UP TO',total,'PAID OpenAI API requests.',flush=True)
    print('The amount charged depends on token usage. This script does NOT guarantee a monetary spending cap.')
    print('Flagged/candidate prompts will be run as supplied. Results need methodological review.')
    print('Exactly ONE response per prompt is preserved. Existing .py/.attempt.json are never overwritten.')
    approval=input(f'Type RUN {total} to approve these {total} paid requests (anything else skips): ').strip()
    if approval != f'RUN {total}':
        print('Paid calls skipped. Running offline checks/exports only.')
        return
    if not os.environ.get('OPENAI_API_KEY'):
        key=getpass.getpass('Paste OpenAI API key (hidden, never stored): ').strip()
        if not key:
            print('No key entered; generation skipped.')
            return
        os.environ['OPENAI_API_KEY']=key
    # Small chunks protect the first-attempt dataset from a system-wide API
    # failure (quota, rate limits, invalid model): stop before reserving all
    # remaining prompts. Requests within a chunk are at most 6.
    abort_remaining=False
    for p,_,pending in datasets:
        if not pending or abort_remaining: continue
        while True:
            _,todo=runner.generate_pending(p)
            if not todo: break
            batch=todo[:min(6,len(todo))]
            batch_stems=[f"{t['problem_id']}_{c}" for t,c in batch]
            print(f'\n{p}: starting next paid chunk of {len(batch_stems)} prompts: '+', '.join(batch_stems),flush=True)
            rc=run_cmd([sys.executable,str(ROOT/'runner_final.py'),'generate','--person',p,
                         '--limit',str(len(batch)),'--workers',str(workers),'--confirm','RUN'])
            _,remaining=runner.generate_pending(p)
            if len(remaining)>=len(todo):
                print('STOP: No progress after generation command. Check API connection / model. No retries attempted.')
                abort_remaining=True;break
            out=ROOT/'outputs'/p
            unsuccessful=[]
            for key in batch_stems:
                if not (out/'generated'/f'{key}.py').is_file():
                    log=out/'logs'/f'{key}.attempt.json'
                    status='missing_attempt'
                    if log.is_file():
                        try:status=runner.read_json(log).get('status','unknown')
                        except Exception:status='invalid_attempt_log'
                    unsuccessful.append((key,status))
            if unsuccessful or rc:
                print('STOP: Some attempted prompts did not return completed Python code:',unsuccessful,
                      'Exit code:',rc,'-- review logs and resume safely; no automatic re-requests.',flush=True)
                abort_remaining=True;break
        runner.export_person(p)
    if abort_remaining:
        print('Remaining API requests NOT issued due to earlier errors. Exports include current status.')
    print('Paid generation section finished. Attempts and errors are preserved; failures are NOT silently retried.')

def evaluate_approved():
    print('\n== Approved-suite evaluation (only for available judge suites) ==',flush=True)
    if not shutil.which('docker'):
        print('Docker not available; official/regression evaluation skipped.')
        return
    for p in PEOPLE:
        ready=sum(runner.test_ready(p,str(t['problem_id']))[0] for t in runner.person_data(p)['tasks'])
        if not ready: continue
        run_cmd([sys.executable,str(ROOT/'runner_final.py'),'evaluate','--person',p,'--limit','90'])

def execute_sample_smoke(per_case_timeout:float):
    print('\n== Smoke-only comparison to prompt examples ==',flush=True)
    if not shutil.which('docker'):
        print('Docker not found; smoke tests skipped. No generated code run on host.')
        return
    if subprocess.run(['docker','image','inspect',runner.CONFIG['docker_image']],capture_output=True).returncode:
        print('Missing Docker image; run: docker pull',runner.CONFIG['docker_image'])
        return
    for p in PEOPLE:
        out=ROOT/'outputs'/p
        out.mkdir(parents=True,exist_ok=True)
        command=['docker','run','--rm','--pull','never','--network','none',
                  '--cpus','2','--memory','512m','--pids-limit','64',
                  '--read-only','--cap-drop','ALL','--security-opt','no-new-privileges',
                  '--user','65534:65534','--tmpfs','/tmp:rw,size=64m',
                  '--mount',f'type=bind,source={ROOT},target=/work,readonly',
                  '--workdir','/tmp',runner.CONFIG['docker_image'],
                  'python','-I','-B','/work/inside_smoke_batch.py',p,str(per_case_timeout)]
        print('Smoke-checking',p,flush=True)
        try:
            cp=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=2000)
            if cp.returncode!=0:
                print('Smoke failed:',cp.stderr[-300:]);continue
            payload=json.loads(cp.stdout)
            results=payload['results']
            # Per-person machine-readable result file (not Pass@1)
            runner.write_json(out/'sample_smoke.json',payload)
            columns=('person','problem_id','condition','sample_run_status','sample_cases_available',
                     'sample_cases_executed','sample_reference_matches','first_nonmatch_index','details',
                     'source','elapsed_seconds')
            with (out/'sample_smoke.csv').open('w',newline='',encoding='utf-8-sig') as f:
                w=csv.DictWriter(f,fieldnames=columns,extrasaction='ignore');w.writeheader();w.writerows(results)
            from collections import Counter
            print(' ',p,'solutions with code',len(results),'sample status:',dict(Counter(r['sample_run_status'] for r in results)),flush=True)
        except (subprocess.TimeoutExpired,ValueError) as ex:
            print('Smoke harness error:',type(ex).__name__,str(ex)[:150])

def export_all():
    print('\n== Export / evidence ==',flush=True)
    for p in PEOPLE:
        runner.export_person(p)
    combined=[]
    for p in PEOPLE:
        folder=ROOT/'outputs'/p
        smoke={}
        smoke_json=folder/'sample_smoke.json'
        if smoke_json.is_file():
            for row in json.loads(smoke_json.read_text('utf-8')).get('results',[]):
                smoke[(str(row['problem_id']),row['condition'])]=row
        with (folder/'results.csv').open(encoding='utf-8-sig',newline='') as f:
            for row in csv.DictReader(f):
                sr=smoke.get((str(row['problem_id']),row['condition']),{})
                row['sample_run_status']=sr.get('sample_run_status','')
                row['sample_cases_executed']=sr.get('sample_cases_executed','')
                row['sample_reference_matches']=sr.get('sample_reference_matches','')
                combined.append(row)
    folder=ROOT/'outputs'
    out=folder/'ALL_270_results.csv'
    with out.open('w',newline='',encoding='utf-8-sig') as f:
        columns=list(combined[0].keys())
        w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(combined)
    from collections import Counter
    categories=dict(Counter(row['status'] for row in combined))
    print('Combined 270-row manifest:',out,'statuses:',categories,flush=True)
    return combined

def archive():
    target=ROOT/'RMT_Final_Evidence.zip'
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for rel in ('outputs','data/sample_tests','data/test_cases','data/person_1_prompts.json',
                    'data/person_2_prompts.json','data/person_3_prompts.json','audit',
                    'config.json','run_all_final.py','runner_final.py','inside_judge_final.py',
                    'inside_smoke_batch.py','prepare_sample_suites.py'):
            src=ROOT/rel
            if src.is_file():z.write(src,rel)
            elif src.is_dir():
                for f in src.rglob('*'):
                    if f.is_file() and f.suffix!='.tmp':z.write(f,f.relative_to(ROOT))
    print('ZIP evidence archive:',target,flush=True)

def main():
    ap=argparse.ArgumentParser(description='Bulk RMT Final, resumable. Official results vs example-only smoke separated.')
    ap.add_argument('--workers',type=int,default=2,help='API concurrent workers (1..3)')
    ap.add_argument('--max-paid',type=int,default=270,help='Maximum additional API requests the user can explicitly authorize')
    ap.add_argument('--no-generate',action='store_true',help='Offline only: evaluate, smoke, export and archive')
    ap.add_argument('--per-case-timeout',type=float,default=4.0)
    args=ap.parse_args()
    if args.workers not in (1,2,3):ap.error('--workers must be 1..3')
    if not 0 < args.per_case_timeout <= 20:ap.error('invalid timeout')
    print('RMT Final batch runner (safe to rerun).',flush=True)
    print('Already saved attempts and generated programs will NOT be regenerated.',flush=True)
    if args.no_generate:
        preflight_count()
    else:
        generate_all(args.workers,args.max_paid)
    real_check()
    evaluate_approved()
    execute_sample_smoke(args.per_case_timeout)
    combined=export_all()
    archive()
    print('\nDONE. Evidence ZIP and 3 per-person result CSVs created.')
    print('Reminder: sample_run_status is NOT Pass@1. Blank pass_at_1 means NOT EVALUATED on approved tests.')

if __name__=='__main__':
    main()
