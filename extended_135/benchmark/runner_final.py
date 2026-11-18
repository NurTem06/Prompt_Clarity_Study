"""RMT Final: isolated first-attempt API generation and offline evaluation.

No network calls happen outside the explicit `generate` subcommand.
No new tests are supplied with this package; Pass@1 remains blank until
separate complete, approved test suites are imported.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
PEOPLE = ('person_1', 'person_2', 'person_3')
CONDITIONS = ('clear', 'ambiguous')
FIELDNAMES = [
    'person', 'problem_id', 'difficulty_tier', 'tier_source', 'condition',
    'original_condition_label', 'status', 'model', 'reasoning_effort', 'temperature',
    'top_p', 'generated_code_file', 'syntax_ok', 'test_cases_total',
    'test_cases_executed', 'test_cases_passed', 'first_failed_case', 'pass_at_1',
    'failure_type', 'runtime_seconds', 'error_details', 'checker',
    'checker_review_status', 'test_source', 'prompt_sha256', 'code_sha256',
    'api_response_id', 'input_tokens', 'output_tokens', 'api_request_status',
    'generated_at_utc', 'evaluated_at_utc'
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def person_data(person: str):
    path = ROOT / 'data' / f'{person}_prompts.json'
    doc = read_json(path)
    tasks = doc['tasks']
    assert len(tasks) == 45, (person, len(tasks))
    assert len({str(t['problem_id']) for t in tasks}) == 45
    for t in tasks:
        for c in CONDITIONS:
            assert t[c + '_prompt'].strip()
            assert sha(t[c + '_prompt']) == t[c + '_sha256']
    return doc


def output_dirs(person: str):
    d = ROOT / 'outputs' / person
    for sub in ('generated', 'logs', 'results'):
        (d / sub).mkdir(parents=True, exist_ok=True)
    return d


def task_selection(person: str, task_id: str | None):
    doc = person_data(person)
    tasks = [t for t in doc['tasks'] if task_id is None or str(t['problem_id']) == str(task_id)]
    if task_id is not None and not tasks:
        raise SystemExit(f'Unknown task ID {task_id} in {person}.')
    return doc, tasks


def test_path(person: str, task_id: str) -> Path:
    return ROOT / 'data' / 'test_cases' / person / f'{task_id}.json'


def test_ready(person: str, task_id: str):
    path = test_path(person, task_id)
    if not path.is_file():
        return False, 'missing_test_suite', None
    try:
        obj = read_json(path)
        a, b = obj.get('inputs'), obj.get('outputs')
        if (str(obj.get('problem_id')) != str(task_id) or not isinstance(a,list)
            or not isinstance(b,list) or not a or len(a) != len(b)
            or not all(isinstance(v,str) for v in a+b)):
            return False,'invalid_test_suite',None
        if obj.get('review_status') != 'approved':
            return False,'tests_not_approved',obj
        checker = obj.get('checker')
        if checker not in ('reference_tokens', 'numeric_tolerance', 'semantic'):
            return False,'checker_not_configured',obj
        if checker == 'numeric_tolerance' and (not isinstance(obj.get('abs_tol'),(int,float)) or not isinstance(obj.get('rel_tol'),(int,float))):
            return False,'missing_numeric_tolerances',obj
        if checker == 'semantic' and not (ROOT/'data'/'checkers'/f'{person}_{task_id}.py').is_file():
            return False,'missing_semantic_checker',obj
        return True,'ready',obj
    except (ValueError, OSError, TypeError):
        return False,'invalid_test_json',None


def make_pairs(person: str, task_id=None, condition='both'):
    doc, tasks = task_selection(person, task_id)
    conds = CONDITIONS if condition == 'both' else (condition,)
    return doc, [(t, c) for t in tasks for c in conds]


def generate_pending(person: str, task_id=None, condition='both'):
    doc, pairs = make_pairs(person, task_id, condition)
    base = output_dirs(person)
    pending=[]
    for t,c in pairs:
        stem=f"{t['problem_id']}_{c}"
        if not (base/'generated'/f'{stem}.py').exists() and not (base/'logs'/f'{stem}.attempt.json').exists():
            pending.append((t,c))
    return doc, pending


def preflight(args):
    all_ids=[]
    for person in PEOPLE:
        doc = person_data(person)
        levels={level:sum(t['difficulty_tier'].lower()==level for t in doc['tasks']) for level in ('introductory','interview','competition')}
        flagged=sum(bool(t['audit_flags']) for t in doc['tasks'])
        missing=sum(not test_ready(person,str(t['problem_id']))[0] for t in doc['tasks'])
        all_ids.extend(str(t['problem_id']) for t in doc['tasks'])
        print(f"{person}: {len(doc['tasks'])} tasks, 90 prompts, tiers={levels}, flagged_tasks={flagged}, approved_test_suites={45-missing}/45")
    print('Unique IDs across people:',len(set(all_ids)),'/ 135')
    print('Model copied from old pipeline:',CONFIG['model'],'| reasoning:',CONFIG['reasoning'])
    print('API calls issued by preflight: ZERO')


def status(args):
    for person in (PEOPLE if args.person=='all' else (args.person,)):
        doc = person_data(person)
        base = output_dirs(person)
        counts = {'generated':0,'attempted':0,'evaluated':0,'approved_suites':0,'total_suite_cases':0}
        bycond={c:{'evaluated':0,'passed':0} for c in CONDITIONS}
        for t in doc['tasks']:
            ok,reason,tests=test_ready(person,str(t['problem_id']))
            if ok:
                counts['approved_suites']+=1
                counts['total_suite_cases']+=len(tests['inputs'])
            for c in CONDITIONS:
                stem=f"{t['problem_id']}_{c}"
                if (base/'generated'/f'{stem}.py').is_file():counts['generated']+=1
                if (base/'logs'/f'{stem}.attempt.json').is_file():counts['attempted']+=1
                res=base/'results'/f'{stem}.json'
                if res.is_file():
                    result=read_json(res)
                    if result.get('failure_type') != 'checker_error' and result.get('pass_at_1') in (0,1):
                        counts['evaluated']+=1
                        bycond[c]['evaluated']+=1
                        bycond[c]['passed']+=int(result['pass_at_1'])
        print(f"{person}: generated {counts['generated']}/90, attempts {counts['attempted']}/90, evaluated {counts['evaluated']}/90, approved test suites {counts['approved_suites']}/45 ({counts['total_suite_cases']} cases)")
        for c in CONDITIONS:
            print('  ',c,':',bycond[c]['passed'],'passed of',bycond[c]['evaluated'],'actually evaluated (NOT out of 45)')
    print('This command sends ZERO API requests.')


def dry_run(args):
    doc,pending=generate_pending(args.person,args.task,args.condition)
    print('Person:',args.person,'| total pending:',len(pending),'| queued with --limit:',min(len(pending),args.limit))
    for t,c in pending[:args.limit]:
        print(f" - {t['problem_id']}_{c} | {t['difficulty_tier']} | audit_flags={','.join(t['audit_flags']) or 'none'} | sha256={t[c+'_sha256'][:12]}")
    if not pending:print('No unattempted prompts remain.')
    print('This command sends ZERO API requests.')


def generate(args):
    if args.limit < 1:raise SystemExit('--limit must be >=1')
    if args.workers < 1 or args.workers > CONFIG['max_workers']:
        raise SystemExit(f'--workers must be in 1..{CONFIG["max_workers"]}')
    doc,pending=generate_pending(args.person,args.task,args.condition)
    pending=pending[:args.limit]
    if not pending:
        print('Nothing to generate. First attempts are preserved.');return
    print(f"Selected {len(pending)} FIRST-ATTEMPT PAID API requests; model={CONFIG['model']}; reasoning={CONFIG['reasoning']}")
    print('Pairs:',', '.join(f"{t['problem_id']}_{c}" for t,c in pending))
    flagged=[f"{t['problem_id']}_{c}" for t,c in pending if t['audit_flags']]
    if flagged:print('WARNING: selected prompt(s) have audit flags:',', '.join(flagged))
    missing=[f"{t['problem_id']}_{c}" for t,c in pending if not test_ready(args.person,str(t['problem_id']))[0]]
    if missing: print('WARNING: no approved test suite for',len(missing),'selected prompt(s); code can be generated but cannot be scored yet.')
    if args.confirm != 'RUN':
        raise SystemExit('PAID generation not started. Add --confirm RUN after reviewing dry-run and audit flags.')
    if not os.environ.get('OPENAI_API_KEY'):
        raise SystemExit('OPENAI_API_KEY is absent in this PowerShell session. No requests sent.')
    try:
        from openai import OpenAI
    except ImportError:
        raise SystemExit('Install dependency: py -m pip install -r requirements.txt')
    base=output_dirs(args.person)
    # Reserve each first-attempt log JUST BEFORE its request starts. If a long
    # batch is interrupted, queued/unstarted work remains eligible next time.
    request_items=[(f"{t['problem_id']}_{c}",t,c) for t,c in pending]

    def call_one(item):
        key,t,c=item
        attempt=base/'logs'/f'{key}.attempt.json'
        code=base/'generated'/f'{key}.py'
        if code.exists():return key,'already_generated_skip'
        prompt=t[f'{c}_prompt']
        record={'person':args.person,'problem_id':t['problem_id'],'condition':c,'difficulty_tier':t['difficulty_tier'],
                'model_requested':CONFIG['model'],'reasoning':CONFIG['reasoning'],
                'max_output_tokens':CONFIG['max_output_tokens'],
                'system_message':doc['common_system_message'],
                'prompt_sha256':sha(prompt),'source_file_sha256':doc['source_sha256'],
                'audit_flags':t['audit_flags'],
                'started_at_utc':datetime.now(timezone.utc).isoformat(),
                'status':'request_started',
                'note':'Request may have incurred a charge even if no code was saved; do not blindly retry.'}
        try:
            with attempt.open('x',encoding='utf-8') as f:
                json.dump(record,f,ensure_ascii=False,indent=2)
        except FileExistsError:
            return key,'existing_attempt_skip'
        client=OpenAI(max_retries=0,timeout=300.0)
        try:
            resp=client.responses.create(
                model=CONFIG['model'], reasoning=CONFIG['reasoning'],
                instructions=doc['common_system_message'],input=t[f'{c}_prompt'],
                max_output_tokens=CONFIG['max_output_tokens'],store=False,tools=[])
            record.update(status=resp.status,model_returned=resp.model,
                          response_id=resp.id,usage=resp.usage.model_dump() if resp.usage else {},
                          finished_at_utc=datetime.now(timezone.utc).isoformat())
            write_json(base/'logs'/f'{key}.response.json',resp.model_dump())
            write_json(base/'logs'/f'{key}.attempt.json',record)
            if resp.status!='completed':return key,'incomplete_'+str(resp.status)
            output=resp.output_text
            if not output or not output.strip():return key,'empty_output'
            (base/'generated'/f'{key}.py').write_text(output,encoding='utf-8')
            return key,f'saved {len(output)} characters'
        except Exception as ex:
            record.update(status='request_error',error_type=type(ex).__name__,
                          error_message=str(ex)[:500],finished_at_utc=datetime.now(timezone.utc).isoformat())
            write_json(base/'logs'/f'{key}.attempt.json',record)
            return key,f'ERROR {type(ex).__name__}: {str(ex)[:160]}'

    print('Starting paid requests:',len(request_items),flush=True)
    if args.workers == 1:
        for item in request_items:
            key,result=call_one(item)
            print(key,result,flush=True)
            if result.startswith('ERROR') or result.startswith('incomplete'):
                print('Stopped serial generation. Inspect log before retry.');break
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures={pool.submit(call_one,item):item[0] for item in request_items}
            for future in as_completed(futures):
                key,result=future.result()
                print(key,result,flush=True)
    export_person(args.person)
    print('Next: py runner_final.py status --person',args.person)


def evaluate(args):
    if args.limit<1:raise SystemExit('--limit must be >=1')
    if not shutil.which('docker'):
        raise SystemExit('Docker not found. Install/start Docker Desktop and pull python:3.11-slim.')
    if subprocess.run(['docker','image','inspect',CONFIG['docker_image']],capture_output=True).returncode:
        raise SystemExit('Docker image unavailable. Run: docker pull python:3.11-slim')
    _,pairs=make_pairs(args.person,args.task,args.condition)
    base=output_dirs(args.person)
    todo=[]
    skipped=[]
    for t,c in pairs:
        key=f"{t['problem_id']}_{c}"
        if (base/'results'/f'{key}.json').is_file():continue
        if not (base/'generated'/f'{key}.py').is_file():continue
        ready,why,tests=test_ready(args.person,str(t['problem_id']))
        if not ready:
            skipped.append((key,why))
            continue
        todo.append((t,c,tests))
    if not todo:
        print('No runnable NEW evaluations; generated solutions or approved test suites/checkers are missing.')
        for key,why in skipped[:8]: print(' skipped',key,why)
        return
    for t,c,tests in todo[:args.limit]:
        key=f"{t['problem_id']}_{c}"
        code=base/'generated'/f'{key}.py'
        suite=test_path(args.person,str(t['problem_id']))
        rel_code=code.relative_to(ROOT).as_posix()
        rel_suite=suite.relative_to(ROOT).as_posix()
        command=['docker','run','--rm','--pull','never','--network','none',
                 '--cpus','1','--memory','512m','--pids-limit','64','--read-only',
                 '--cap-drop','ALL','--security-opt','no-new-privileges',
                 '--user','65534:65534','--tmpfs','/tmp:rw,size=64m',
                 '--mount',f'type=bind,source={ROOT},target=/work,readonly',
                 '--workdir','/tmp',CONFIG['docker_image'],
                 'python','-I','-B','/work/inside_judge_final.py',
                 '/work/'+rel_code,'/work/'+rel_suite,
                 args.person,str(t['problem_id']),str(CONFIG['case_timeout_seconds'])]
        print('Judging',key,'with',len(tests['inputs']),'approved cases; checker=',tests['checker'],flush=True)
        try:
            cp=subprocess.run(command,capture_output=True,text=True,
                              timeout=CONFIG['task_timeout_seconds'])
        except subprocess.TimeoutExpired:
            print('Task-level timeout:',key)
            continue
        if cp.returncode != 0:
            print('Judge error:',cp.stderr[-500:])
            continue
        try:result=json.loads(cp.stdout)
        except ValueError:
            print('Non-JSON judge output:',cp.stdout[-300:]);continue
        result.update(person=args.person,condition=c,difficulty_tier=t['difficulty_tier'],
                      model=CONFIG['model'],checker_review_status=tests['review_status'],
                      test_source=tests.get('test_source',''),
                      prompt_sha256=t[c+'_sha256'],code_sha256=sha(code.read_text('utf-8')),
                      evaluated_at_utc=datetime.now(timezone.utc).isoformat())
        write_json(base/'results'/f'{key}.json',result)
        print(' ',key,'Pass@1=',result['pass_at_1'],'passed=',result['test_cases_passed'],
              '/',result['total_test_cases'],'failure=',result.get('failure_type') or 'none')
    export_person(args.person)


def export_person(person: str):
    doc=person_data(person);base=output_dirs(person)
    rows=[]
    for t in doc['tasks']:
        for c in CONDITIONS:
            key=f"{t['problem_id']}_{c}"
            code_path=base/'generated'/f'{key}.py'
            attempt_path=base/'logs'/f'{key}.attempt.json'
            result_path=base/'results'/f'{key}.json'
            attempt=read_json(attempt_path) if attempt_path.is_file() else {}
            result=read_json(result_path) if result_path.is_file() else {}
            usage=attempt.get('usage') or {}
            ready,reason,tests=test_ready(person,str(t['problem_id']))
            status=('CHECKER_ERROR' if result.get('failure_type')=='checker_error' else 'EVALUATED') if result else ('GENERATED_UNTESTED' if code_path.is_file() else ('ATTEMPT_LOG_ONLY' if attempt else 'NOT_RUN'))
            code_sha=sha(code_path.read_text('utf-8')) if code_path.is_file() else ''
            row={
                'person':person,'problem_id':t['problem_id'],
                'difficulty_tier':t['difficulty_tier'],'tier_source':t['tier_source'],
                'condition':c,'original_condition_label':'Clear' if c=='clear' else t['original_ambiguous_label'],
                'status':status,'model':attempt.get('model_returned') or attempt.get('model_requested') or '',
                'reasoning_effort':attempt.get('reasoning',{}).get('effort',''),
                'temperature':'','top_p':'',
                'generated_code_file':str(code_path.relative_to(ROOT)) if code_path.is_file() else '',
                'syntax_ok':result.get('syntax_ok',''),
                'test_cases_total':result.get('total_test_cases',len(tests['inputs']) if ready else ''),
                'test_cases_executed':result.get('test_cases_executed',''),
                'test_cases_passed':result.get('test_cases_passed',''),
                'first_failed_case':result.get('failure_index_1based') or '',
                'pass_at_1':result.get('pass_at_1','') if status=='EVALUATED' else '',
                'failure_type':result.get('failure_type') or '',
                'runtime_seconds':result.get('runtime_seconds',''),
                'error_details':result.get('detail') or attempt.get('error_message') or '',
                'checker':result.get('checker') or (tests.get('checker','') if tests else ''),
                'checker_review_status':result.get('checker_review_status') or (tests.get('review_status','') if tests else ''),
                'test_source':result.get('test_source') or (tests.get('test_source','') if tests else ''),
                'prompt_sha256':t[c+'_sha256'],'code_sha256':code_sha,
                'api_response_id':attempt.get('response_id',''),
                'input_tokens':usage.get('input_tokens',''),'output_tokens':usage.get('output_tokens',''),
                'api_request_status':attempt.get('status',''),
                'generated_at_utc':attempt.get('finished_at_utc',''),
                'evaluated_at_utc':result.get('evaluated_at_utc','')}
            rows.append(row)
    target=base/'results.csv'
    with target.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDNAMES)
        writer.writeheader();writer.writerows(rows)
    successes={c:[r for r in rows if r['condition']==c and r['status']=='EVALUATED'] for c in CONDITIONS}
    summary={
        'person':person,'task_count':45,'rows':len(rows),
        'generated':sum(r['generated_code_file']!='' for r in rows),
        'evaluated':sum(r['status']=='EVALUATED' for r in rows),
        'results_by_condition':{c:{'evaluated':len(successes[c]),'passed':sum(int(r['pass_at_1']) for r in successes[c])} for c in CONDITIONS},
        'scoring_note':'Only approved supplied test suites; no result exists for NOT_RUN or GENERATED_UNTESTED rows.',
        'created_at_utc':datetime.now(timezone.utc).isoformat()}
    write_json(base/'summary.json',summary)
    return target


def export(args):
    for person in PEOPLE if args.person=='all' else (args.person,):
        path=export_person(person)
        print('Exported',path.relative_to(ROOT),'(90 rows; no invented results)')


def main():
    p=argparse.ArgumentParser(description='RMT Final controlled, auditable, first-attempt generation.')
    commands=p.add_subparsers(dest='command',required=True)
    commands.add_parser('preflight')
    ps=commands.add_parser('status')
    ps.add_argument('--person',choices=(*PEOPLE,'all'),default='all')
    pd=commands.add_parser('dry-run')
    pd.add_argument('--person',choices=PEOPLE,required=True)
    pd.add_argument('--task')
    pd.add_argument('--condition',choices=(*CONDITIONS,'both'),default='both')
    pd.add_argument('--limit',type=int,default=2)
    pg=commands.add_parser('generate')
    pg.add_argument('--person',choices=PEOPLE,required=True)
    pg.add_argument('--task')
    pg.add_argument('--condition',choices=(*CONDITIONS,'both'),default='both')
    pg.add_argument('--limit',type=int,default=2)
    pg.add_argument('--workers',type=int,default=1)
    pg.add_argument('--confirm',default='',help='Must be exactly RUN, because requests incur charges')
    pe=commands.add_parser('evaluate')
    pe.add_argument('--person',choices=PEOPLE,required=True)
    pe.add_argument('--task')
    pe.add_argument('--condition',choices=(*CONDITIONS,'both'),default='both')
    pe.add_argument('--limit',type=int,default=2)
    px=commands.add_parser('export')
    px.add_argument('--person',choices=(*PEOPLE,'all'),default='all')
    args=p.parse_args()
    {'preflight':preflight,'status':status,'dry-run':dry_run,'generate':generate,'evaluate':evaluate,'export':export}[args.command](args)


if __name__=='__main__':main()
