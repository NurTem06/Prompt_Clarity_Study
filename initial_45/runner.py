"""RMT batch generation & Docker evaluation. Uses paid OpenAI API only for 'generate'."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
DATAFILE = BASE/'data'/'tasks.json'
GEN = BASE/'generated'; LOG = BASE/'logs'; RESULTS = BASE/'results'
MODEL='gpt-6.1-sol'
REASONING={'mode':'standard','effort':'medium'}
MAX_OUTPUT_TOKENS=16000
DOCKER_IMAGE='python:3.11-slim'


def load():
    return json.loads(DATAFILE.read_text(encoding='utf-8'))


def save_json(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')


def stem(task,condition):
    return f"{task['problem_id']}_{condition}"


def eligible(task):
    return (task.get('test_cases') is not None
            and 'source_description_contradiction: exclude until resolved identically' not in task.get('notes',[])
            and (task.get('source_group') != 'revised_15' or task.get('review_status') in ('approved_by_two_independent_reviewers', 'exploratory_unreviewed')))


def status(args):
    tasks=load()
    print('Total tasks:',len(tasks),'| prompts:',len(tasks)*2)
    print('Tasks with test sets:',sum(eligible(t) for t in tasks),'| pending test/review:',sum(not eligible(t) for t in tasks))
    for level in ['introductory','interview','competition']:
        group=[t for t in tasks if t['difficulty']==level]
        code=sum((GEN/f'{t["problem_id"]}_{c}.py').exists() for t in group for c in ('clear','ambiguous'))
        evaluated=sum((RESULTS/f'{t["problem_id"]}_{c}.json').exists() for t in group for c in ('clear','ambiguous'))
        print(f'  {level:13} tasks={len(group)} with_tests={sum(eligible(t) for t in group)} generated={code}/30 evaluated={evaluated}/30')
    print('\nNEXT:  py runner.py generate --limit 2    (2 paid requests)')
    print('THEN:  py runner.py evaluate --limit 2    (no API charges)')
    print('THEN:  py runner.py export                (no API charges)')


def selected_tasks(args):
    tasks=load()
    if getattr(args,'task',None) is not None:
        tasks=[x for x in tasks if x['problem_id']==args.task]
        if not tasks:raise SystemExit('Task ID not in the 45-task dataset')
    return tasks


def generate(args):
    if args.limit<1:raise SystemExit('--limit must be at least 1')
    if not os.environ.get('OPENAI_API_KEY'):
        raise SystemExit('OPENAI_API_KEY not set in this PowerShell session.')
    try:from openai import OpenAI
    except ImportError:raise SystemExit('Install package first: py -m pip install -r requirements.txt')
    tasks=selected_tasks(args)
    pending=[]
    for t in tasks:
        if not eligible(t):continue
        for cond in ('clear','ambiguous'):
            key=stem(t,cond)
            if (GEN/f'{key}.py').exists():continue
            if (LOG/f'{key}.attempt.json').exists():continue
            pending.append((t,cond))
    pending=pending[:args.limit]
    if not pending:
        print('No eligible unattempted prompts. Existing code and attempts have been preserved.')
        return
    print(f'About to send {len(pending)} PAID first-attempt API request(s) using {MODEL}.')
    print('Queued:',', '.join(stem(t,c) for t,c in pending))
    print('Only eligible tasks are generated. Exploratory unreviewed pairs are labeled in the dataset.')
    if not args.yes:
        reply=input('Type RUN to confirm paid requests: ').strip()
        if reply!='RUN':
            print('Cancelled without sending requests.')
            return
    client=OpenAI(max_retries=0,timeout=300.0)
    for t,cond in pending:
        key=stem(t,cond); codefile=GEN/f'{key}.py'; attempt=LOG/f'{key}.attempt.json'
        prompt=t['clear_prompt'] if cond=='clear' else t['ambiguous_prompt']
        if codefile.exists() or attempt.exists():
            print('Skipping existing attempt:',key);continue
        record={'problem_id':t['problem_id'],'condition':cond,'difficulty':t['difficulty'],
                'model_requested':MODEL,'reasoning':REASONING,'max_output_tokens':MAX_OUTPUT_TOKENS,
                'system_message':t['system_message'],'prompt_sha256':hashlib.sha256(prompt.encode('utf-8')).hexdigest(),
                'started_at_utc':datetime.now(timezone.utc).isoformat(),'status':'request_started',
                'note':'A request may have incurred charges, even if code was not saved. Do not silently retry.'}
        save_json(attempt,record)
        print(f'Submitting {key}...',flush=True)
        try:
            response=client.responses.create(model=MODEL,reasoning=REASONING,
                instructions=t['system_message'],input=prompt,max_output_tokens=MAX_OUTPUT_TOKENS,
                store=False,tools=[])
            record.update(status=response.status,model_returned=response.model,response_id=response.id,
                          usage=response.usage.model_dump() if response.usage else None,
                          finished_at_utc=datetime.now(timezone.utc).isoformat())
            save_json(LOG/f'{key}.response.json',response.model_dump())
            save_json(attempt,record)
            if response.status!='completed':
                print('Response incomplete. Saved logs. Stopping; do not auto-retry.',file=sys.stderr)
                return
            code=response.output_text
            codefile.write_text(code,encoding='utf-8')
            print('Saved:',codefile.relative_to(BASE),'characters=',len(code),flush=True)
        except Exception as ex:
            record.update(status='request_error',error_type=type(ex).__name__,
                          error_message=str(ex)[:500],finished_at_utc=datetime.now(timezone.utc).isoformat())
            save_json(attempt,record)
            print('STOPPED:',type(ex).__name__,str(ex)[:500],file=sys.stderr)
            print('Check attempt log before deciding whether to retry; do not delete blindly.',file=sys.stderr)
            return
    print('Generation batch complete. Next: py runner.py evaluate --limit',args.limit)


def evaluate(args):
    if args.limit<1:raise SystemExit('--limit must be at least 1')
    if not shutil.which('docker'):raise SystemExit('Docker Desktop not found. Start Docker and run docker pull python:3.11-slim')
    check=subprocess.run(['docker','image','inspect',DOCKER_IMAGE],capture_output=True,text=True)
    if check.returncode:
        raise SystemExit('Docker image missing or engine stopped. Run: docker pull python:3.11-slim')
    tasks=selected_tasks(args)
    pending=[]
    for t in tasks:
        if not eligible(t):continue
        for cond in ('clear','ambiguous'):
            key=stem(t,cond)
            if (GEN/f'{key}.py').exists() and not (RESULTS/f'{key}.json').exists():pending.append((t,cond))
    for t,cond in pending[:args.limit]:
        key=stem(t,cond)
        taskfile=BASE/'data'/'single_task.json'
        # This file is fixed before each Docker invocation and treated as read-only in container.
        save_json(taskfile,t)
        argslist=['docker','run','--rm','--pull','never','--network','none',
              '--cpus','1','--memory','512m','--pids-limit','64','--read-only',
              '--cap-drop','ALL','--security-opt','no-new-privileges',
              '--user','65534:65534','--tmpfs','/tmp:rw,size=64m',
              '--mount',f'type=bind,source={BASE},target=/work,readonly',
              '--workdir','/work',DOCKER_IMAGE,'python','-I','-B',
              '/work/inside_judge.py',f'/work/generated/{key}.py','/work/data/single_task.json']
        print('Judging',key,'...',flush=True)
        try:p=subprocess.run(argslist,capture_output=True,text=True,timeout=1200)
        except subprocess.TimeoutExpired:
            print('Docker judge exceeded whole-task time; flag for review:',key)
            continue
        if p.returncode:
            print('Docker evaluation failed:',p.stderr[-800:]);continue
        try:result=json.loads(p.stdout)
        except ValueError:
            print('Invalid judge output:',p.stdout[-300:]);continue
        result.update(condition=cond,difficulty=t['difficulty'],
                      model=MODEL,provenance='batch_runner',checked_at_utc=datetime.now(timezone.utc).isoformat())
        save_json(RESULTS/f'{key}.json',result)
        print(f"{key}: Pass@1={result['pass_at_1']} passed={result['passed_before_first_failure']}/{result['total_test_cases']} failure={result['failure_type'] or 'none'}")
    taskfile=BASE/'data'/'single_task.json'
    if taskfile.exists():taskfile.unlink()
    print('Evaluation batch finished. Next: py runner.py export')


def export(args):
    tasks=load(); rows=[]
    for t in tasks:
        for cond in ['clear','ambiguous']:
            key=stem(t,cond)
            path=RESULTS/f'{key}.json'
            result=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
            apath=LOG/f'{key}.attempt.json'
            attempt=json.loads(apath.read_text(encoding='utf-8')) if apath.exists() else {}
            usage=attempt.get('usage') or {}
            rows.append({'problem_id':t['problem_id'],'difficulty':t['difficulty'],'condition':cond,
                'has_tests':bool(t['test_cases']),'test_count':len(t['test_cases']['inputs']) if t['test_cases'] else '',
                'has_generated_code':(GEN/f'{key}.py').exists(),
                'pass_at_1':result.get('pass_at_1',''),
                'passed_before_first_failure':result.get('passed_before_first_failure',''),
                'failure_type':result.get('failure_type') or '',
                'failure_index_1based':result.get('failure_index_1based') or '',
                'checker':result.get('checker') or '',
                'model':attempt.get('model_returned') or (MODEL if (GEN/f'{key}.py').exists() else ''),
                'input_tokens':usage.get('input_tokens',''),'output_tokens':usage.get('output_tokens',''),
                'review_status':t['review_status'],'source_group':t['source_group'],
                'provenance':result.get('provenance',''),'notes':'; '.join(t['notes'])})
    target=BASE/'results.csv'
    with target.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    summary={}
    for level in ['introductory','interview','competition']:
        subset=[t for t in tasks if t['difficulty']==level]
        paired=[]
        for t in subset:
            c=RESULTS/f"{t['problem_id']}_clear.json";a=RESULTS/f"{t['problem_id']}_ambiguous.json"
            if c.exists() and a.exists():
                cval=json.loads(c.read_text())['pass_at_1'];aval=json.loads(a.read_text())['pass_at_1']
                paired.append((cval,aval))
        summary[level]={'total_tasks':len(subset),'paired_tasks_evaluated':len(paired),
                        'clear_pass_at_1':(sum(c for c,a in paired)/len(paired) if paired else None),
                        'ambiguous_pass_at_1':(sum(a for c,a in paired)/len(paired) if paired else None),
                        'discordant_clear_only':sum(c==1 and a==0 for c,a in paired),
                        'discordant_ambiguous_only':sum(c==0 and a==1 for c,a in paired)}
    save_json(BASE/'summary.json',{'scope':'available test suites only',
        'warning':'Not a final study result until all selected tasks have independently reviewed prompt pairs and valid test suites.',
        'tiers':summary})
    print('Saved results.csv and summary.json.')
    for tier,x in summary.items():
        print(tier,'pairs=',x['paired_tasks_evaluated'],'clear=',x['clear_pass_at_1'],'ambiguous=',x['ambiguous_pass_at_1'])


def attach_tests(args):
    external=json.loads(Path(args.file).read_text(encoding='utf-8'))
    if not isinstance(external,list):raise SystemExit('Expected JSON list of APPS records with problem_id and input_output')
    idx={int(t['problem_id']):t for t in external}
    tasks=load();updated=[]
    for t in tasks:
        if t['test_cases'] is not None or t['problem_id'] not in idx:continue
        rec=idx[t['problem_id']]
        if 'source_description_contradiction: exclude until resolved identically' in t['notes']:
            print('Skipping task 4005: inherited source contradiction not resolved');continue
        io=rec.get('input_output')
        try:tests=json.loads(io) if isinstance(io,str) else io
        except Exception:print('Invalid tests for',t['problem_id']);continue
        if not isinstance(tests,dict) or not tests.get('inputs') or len(tests['inputs'])!=len(tests.get('outputs',[])):
            print('Invalid tests for',t['problem_id']);continue
        t['test_cases']=tests
        t['notes']=[n for n in t['notes'] if n!='missing_executable_test_cases']
        updated.append(t['problem_id'])
    if updated:save_json(DATAFILE,tasks)
    print('Attached available tests for:',updated)
    print('IMPORTANT: independent prompt-pair review is still necessary.')


def approve_review(args):
    tasks=load()
    match=next((t for t in tasks if t['problem_id']==args.task),None)
    if not match:raise SystemExit('Task not found')
    if match['source_group']!='revised_15':
        raise SystemExit('This command is only for revised_15 prompt pairs.')
    if args.reviewer1.strip().lower()==args.reviewer2.strip().lower():
        raise SystemExit('Two different reviewers are required.')
    if 'source_description_contradiction: exclude until resolved identically' in match['notes']:
        raise SystemExit('Task 4005 must first resolve the contradictory benchmark statement in both prompts.')
    if match['test_cases'] is None:
        raise SystemExit('Attach official tests first. See: py runner.py attach-tests PATH')
    match['review_status']='approved_by_two_independent_reviewers'
    match['reviewers']=[args.reviewer1.strip(),args.reviewer2.strip()]
    match['reviewed_at_utc']=datetime.now(timezone.utc).isoformat()
    match['notes']=[x for x in match['notes'] if x!='independent_prompt_review_required']
    save_json(DATAFILE,tasks)
    print('Approved revised prompt pair:',args.task,'by',args.reviewer1,'and',args.reviewer2)


def main():
    p=argparse.ArgumentParser(description='RMT experiment: 45 paired APPS-style tasks; safely resume without re-generating first attempts.')
    s=p.add_subparsers(dest='command',required=True)
    s.add_parser('status')
    g=s.add_parser('generate');g.add_argument('--limit',type=int,default=2);g.add_argument('--task',type=int,default=None);g.add_argument('--yes',action='store_true')
    e=s.add_parser('evaluate');e.add_argument('--limit',type=int,default=2);e.add_argument('--task',type=int,default=None)
    s.add_parser('export')
    a=s.add_parser('attach-tests');a.add_argument('file')
    v=s.add_parser('approve-review');v.add_argument('--task',required=True,type=int);v.add_argument('--reviewer1',required=True);v.add_argument('--reviewer2',required=True)
    args=p.parse_args()
    {'status':status,'generate':generate,'evaluate':evaluate,'export':export,'attach-tests':attach_tests,'approve-review':approve_review}[args.command](args)

if __name__=='__main__':main()
