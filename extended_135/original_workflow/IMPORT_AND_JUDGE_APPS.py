"""RMT Final: obtain APPS test-split cases and evaluate saved first-attempt code.

No OpenAI calls. Original project files are not modified. Official APPS inputs/outputs
are acquired from Hugging Face, not generated from model answers. The copied
benchmark workspace has independent results and explicit checker-audit flags.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
from datetime import datetime, timezone
import csv
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from urllib.request import Request, urlopen
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent
BENCH = ROOT / 'RMT_APPS_Benchmark'
SOURCES = ('person_1','person_2','person_3')
CONDITIONS = ('clear','ambiguous')
DATASET = 'metr-evals/apps'
REPO_URL = 'https://huggingface.co/datasets/metr-evals/apps'
API_ROOT = 'https://datasets-server.huggingface.co/rows'

# Every listed ID has been read against supplied prompt text. Tokens alone can reject
# correct constructive answers; only reviewed validators below are semantically scored.
SEMANTIC_VALIDATORS = {
 'person_1': {'4017','4019','28','3028'},
 'person_2': {'4030','4034','4036','4038','4042','4043','4044','43'},
 'person_3': {'4045','4050','4053','45','3053'},
}
NUMERIC_TOLERANCES = {
 'person_2': {'3034':(1e-5,1e-5),'3035':(1e-6,0.0)},
 'person_3': {'3052':(1e-4,0.0),'3059':(1e-6,1e-6)},
}
# Multi-output tasks without validated semantic checkers. Reference-only output
# comparisons are exploratory here and excluded from validated Pass@1 figures.
NEEDS_SEMANTIC_REVIEW = {
 'person_1': set(),
 'person_2': set(),
 'person_3': {'3058'},
}
MULTI_WORDING = re.compile(
 r'(?:\bany\b.{0,45}\b(?:solutions?|answers?|colorings?|strings?|permutations?|trees?|arrangements?|orders?|sequence|array|way|valid|correct|possible|of them|pair|matrix|one of)'
 r'|\b(?:multiple|many|several)\s+(?:possible\s+)?(?:valid\s+)?(?:answers?|solutions?|possibilities|ways)'
 r'|\bin any order\b|you (?:can|may) (?:print|output) any|\boutput any\b)',re.I|re.S)


def utc():return datetime.now(timezone.utc).isoformat()
def checksum(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def dump(path,doc):
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_name(path.name+'.tmp')
 tmp.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 tmp.replace(path)
def load(path):return json.loads(path.read_text(encoding='utf-8'))

def clean_text(x):
 return re.sub(r'[^a-z0-9]+',' ',x.lower()).strip()
def canonical_url(s):
 return re.sub(r'^https?://','',str(s or '')).split('?')[0].strip('/').lower()

def verify_identity(task,row,idx):
 pid=str(task['problem_id'])
 if str(row.get('problem_id',''))!=pid or int(idx)!=int(pid):
  return False,f'wrong APPS ID (requested={pid}, got row={row.get("problem_id")}, idx={idx})'
 expected=canonical_url(task.get('source_problem_url'))
 actual=canonical_url(row.get('url'))
 if expected:
  if expected!=actual:
   return False,f'source URL mismatch: {expected} != {actual}'
  return True,'id_and_url_match'
 # The third participant file omitted source URLs: compare source questions.
 clear=clean_text(task['clear_prompt'])
 question=clean_text(row.get('question') or '')
 if not clear or not question:return False,'source question missing'
 if clear[:180] == question[:180] or clear[:180] in question:
  return True,'id_and_question_exact_prefix'
 similarity=difflib.SequenceMatcher(None,clear[:500],question[:500]).ratio()
 if similarity < .80:
  return False,f'question mismatch (first 500 chars similarity={similarity:.3f})'
 return True,f'id_and_question_similarity_{similarity:.3f}'

def classify(person,task):
 pid=str(task['problem_id'])
 if pid in SEMANTIC_VALIDATORS.get(person,set()):return 'semantic','semantic_checker_reviewed',None
 if pid in NUMERIC_TOLERANCES.get(person,{}):return 'numeric_tolerance','numeric_tolerance_from_problem_statement',NUMERIC_TOLERANCES[person][pid]
 out=task['clear_prompt'].split('-----Output-----',1)[-1].split('-----Examples-----',1)[0].split('-----Sample Input-----',1)[0][:1400]
 if pid in NEEDS_SEMANTIC_REVIEW.get(person,set()) or MULTI_WORDING.search(out):
  return 'reference_tokens','reference_only_multi_output_REQUIRES_REVIEW',None
 return 'reference_tokens','reference_comparison_unique_output_candidate',None

def fetch_row(person,pid):
 # APPS's test split is indexed by APPS problem_id. Always verify the
 # problem_id AND question/URL after retrieval; never assume index == task.
 query=urlencode({'dataset':DATASET,'config':'default','split':'test','offset':int(pid),'length':1})
 url=API_ROOT+'?'+query
 last=''
 for attempt in range(4):
  try:
   req=Request(url,headers={'User-Agent':'RMT-Final-reproducibility/1.0','Accept':'application/json'})
   with urlopen(req,timeout=90) as resp:
    raw=resp.read(80_000_001)
   if len(raw)>=80_000_001:raise ValueError('API response too large (>80 MB); use dataset parquet fallback')
   payload=json.loads(raw)
   rows=payload.get('rows') or []
   if len(rows)!=1:raise ValueError('expected exactly one APPS row, got '+str(len(rows)))
   item=rows[0]
   return item['row'],item.get('row_idx',int(pid)),url
  except Exception as exc:
   last=f'{type(exc).__name__}: {str(exc)[:240]}'
   if attempt<3:time.sleep(2*(attempt+1))
 raise RuntimeError(f'{person}/{pid}: HF dataset viewer failed: {last}')

def normalize_io(value):
 if isinstance(value,str):return json.loads(value)
 if isinstance(value,dict):return value
 raise ValueError(f'unknown input_output type: {type(value).__name__}')

def prepare_bench():
 BENCH.mkdir(exist_ok=True)
 for f in ['runner_final.py','inside_judge_final.py','config.json']:
  if not (ROOT/f).exists():raise FileNotFoundError('Missing required project file: '+str(ROOT/f))
  dest=BENCH/f
  # Never overwrite existing workspace runner and judge silently.
  if not dest.exists():shutil.copy2(ROOT/f,dest)
 for person in SOURCES:
  src=ROOT/'data'/f'{person}_prompts.json'
  if not src.exists():raise FileNotFoundError(str(src))
  (BENCH/'data').mkdir(exist_ok=True)
  dest=BENCH/'data'/src.name
  if not dest.exists():shutil.copy2(src,dest)
  srcout=ROOT/'outputs'/person/'generated'
  if not srcout.exists():raise FileNotFoundError(str(srcout))
  dstout=BENCH/'outputs'/person/'generated'
  dstout.mkdir(parents=True,exist_ok=True)
  for code in srcout.glob('*.py'):
   target=dstout/code.name
   if not target.exists():shutil.copy2(code,target)
   elif checksum(code.read_text(encoding='utf-8'))!=checksum(target.read_text(encoding='utf-8')):
    raise RuntimeError('Code modified since benchmark copy: '+str(target))
 # Copy only checker code from this package; DO NOT execute generated code on host.
 checkers=BENCH/'data'/'checkers'
 checkers.mkdir(parents=True,exist_ok=True)
 for person,ids in SEMANTIC_VALIDATORS.items():
  for pid in ids:
   target=checkers/f'{person}_{pid}.py'
   if not target.exists():
    target.write_text(f'from validated_apps_checkers import validate_{pid} as validate\n',encoding='utf-8')
 source=ROOT/'validated_apps_checkers.py'
 if not source.is_file():raise FileNotFoundError(str(source))
 dest=checkers/'validated_apps_checkers.py'
 shutil.copy2(source,dest)
 # Checker import library from same /work/data/checkers is available via sys.path
 # only when added explicitly by a small wrapper; wrappers are made below.
 for person,ids in SEMANTIC_VALIDATORS.items():
  for pid in ids:
   target=checkers/f'{person}_{pid}.py'
   target.write_text(
    'import sys\nsys.path.insert(0,"/work/data/checkers")\n'
    f'from validated_apps_checkers import validate_{pid} as validate\n',encoding='utf-8')
 return BENCH

def import_one(person,task):
 pid=str(task['problem_id'])
 existing=BENCH/'data'/'test_cases'/person/f'{pid}.json'
 if existing.exists():
  doc=load(existing)
  if doc.get('suite_sha256')!=checksum(json.dumps({'inputs':doc.get('inputs'), 'outputs':doc.get('outputs')},ensure_ascii=False,sort_keys=True)):
   raise ValueError('cached suite checksum mismatch; do not trust modified test data')
  return {'person':person,'problem_id':pid,'status':'CACHED','case_count':len(doc.get('inputs',[])),
          'checker':doc.get('checker',''),'validation_scope':doc.get('validation_scope',''),'detail':''}
 row,idx,url=fetch_row(person,pid)
 ok,reason=verify_identity(task,row,idx)
 if not ok:raise ValueError(reason)
 io=normalize_io(row.get('input_output') or '')
 if io.get('fn_name') not in (None,''):
  raise ValueError('APPS function-call task, not stdin/stdout (fn_name present); separate harness required')
 inputs,outputs=io.get('inputs'),io.get('outputs')
 if not isinstance(inputs,list) or not isinstance(outputs,list) or not inputs or len(inputs)!=len(outputs):
  raise ValueError('APPS test input/output lists empty or unequal')
 if not all(isinstance(s,str) for s in inputs+outputs):
  raise ValueError('APPS test contains non-string input or output; separate harness required')
 method,scope,tols=classify(person,task)
 doc={
  'problem_id':pid,'test_source':f'Original APPS test split via {REPO_URL}; dataset viewer: {url}',
  'source_dataset':DATASET,'source_split':'test','source_problem_url':row.get('url'),
  'retrieved_at_utc':utc(),'verification':reason,
  'review_status':'approved', # authentic dataset reference; special validation caveat in scope
  'validation_scope':scope,'checker':method,
  'inputs':inputs,'outputs':outputs,
 }
 if tols is not None:doc.update(abs_tol=tols[0],rel_tol=tols[1])
 # Store a fingerprint of source inputs+outputs for audit. Uploaded prompts and outputs frozen.
 doc['suite_sha256']=checksum(json.dumps({'inputs':inputs,'outputs':outputs},ensure_ascii=False,sort_keys=True))
 dump(existing,doc)
 return {'person':person,'problem_id':pid,'status':'IMPORTED','case_count':len(inputs),
         'checker':method,'validation_scope':scope,'detail':reason}

def download_phase(workers=3,limit=135):
 tasks=[(p,t) for p in SOURCES for t in load(ROOT/'data'/f'{p}_prompts.json')['tasks']]
 tasks=tasks[:limit]
 log=BENCH/'APPS_import_log.json'
 previous={(r['person'],r['problem_id']):r for r in load(log)} if log.exists() else {}
 todo=tasks  # cached suites are integrity-checked without network requests
 missing=sum(not (BENCH/'data'/'test_cases'/p/f'{t["problem_id"]}.json').exists() for p,t in tasks)
 print(f'APPS download: tasks={len(tasks)}, missing={missing}; no OpenAI API calls',flush=True)
 def job(item):
  p,t=item
  try:return import_one(p,t)
  except Exception as e:
   return {'person':p,'problem_id':str(t['problem_id']),'status':'ERROR','case_count':0,
           'checker':'','validation_scope':'','detail':f'{type(e).__name__}: {str(e)[:320]}'}
 with cf.ThreadPoolExecutor(max_workers=workers) as pool:
  futures={pool.submit(job,item):item for item in todo}
  for future in cf.as_completed(futures):
   result=future.result();previous[(result['person'],result['problem_id'])]=result
   dump(log,[previous[k] for k in sorted(previous)])
   print(result['person'],result['problem_id'],result['status'],result['case_count'],result['detail'][:100],flush=True)
 return previous

def evaluation_phase(workers=2,limit=135):
 if not shutil.which('docker'):raise RuntimeError('Docker CLI not found')
 src=ROOT/'config.json'; image=load(src)['docker_image']
 if subprocess.run(['docker','image','inspect',image],capture_output=True).returncode:
  raise RuntimeError('Docker image missing: run docker pull '+image)
 tasks=[(p,t) for p in SOURCES for t in load(ROOT/'data'/f'{p}_prompts.json')['tasks']]
 tasks=[(p,t) for p,t in tasks if (BENCH/'data'/'test_cases'/p/f'{t["problem_id"]}.json').exists()]
 tasks=tasks[:limit]
 print(f'Offline Docker evaluation: {len(tasks)} tasks / up to {2*len(tasks)} saved programs',flush=True)
 def job(item):
  p,t=item;pid=str(t['problem_id'])
  cmd=[sys.executable,str(BENCH/'runner_final.py'),'evaluate','--person',p,'--task',pid,'--limit','2']
  try:
   cp=subprocess.run(cmd,cwd=BENCH,capture_output=True,text=True,timeout=2700)
   return p,pid,cp.returncode,(cp.stdout+'\n'+cp.stderr)[-1500:]
  except subprocess.TimeoutExpired:return p,pid,124,'Task pair exceeded 45-minute subprocess ceiling'
 with cf.ThreadPoolExecutor(max_workers=workers) as pool:
  for p,pid,code,details in pool.map(job,tasks):
   print('EVALUATE',p,pid,'OK' if code==0 and 'Judge error:' not in details else 'CHECK_LOG',details[-300:].replace('\n',' | '),flush=True)
 write_summary()


def write_markdown_report(summary, rows):
 lines=[
  '# RMT Final — APPS Original Test Case Evaluation',
  '',f"Generated UTC: {summary['created_at_utc']}",
  '', '**Test source:** APPS test split, retrieved by problem_id from Hugging Face metr-evals/apps with verified problem metadata.',
  '', '## Results per person',
  '', '| Person | Tested programs | Benchmark checker passed | Validated denominator | Validated passed |',
  '|---|---:|---:|---:|---:|',
 ]
 for person,d in summary['results_by_person'].items():
  lines.append(f"| {person} | {d['evaluated']}/90 | {d['benchmark_pass']}/{d['benchmark_denominator']} | {d['validated_denominator']} | {d['validated_pass']} |")
 lines.extend(['','## Matched pairs by difficulty','','| Participant / tier | Validated pairs | Both pass | Clear only | Ambiguous only | Both fail |','|---|---:|---:|---:|---:|---:|'])
 for key,d in summary['paired_by_tier'].items():
  lines.append(f"| {key} | {d['fully_validated_pairs']} | {d['both_pass']} | {d['clear_only']} | {d['ambiguous_only']} | {d['both_fail']} |")
 lines.extend(['','## Methodological qualifications','',
 '1. All generated solutions were frozen before retrieving test cases. No new OpenAI requests are made.',
 '2. All available **APPS dataset inputs/outputs** are used; they are not merely the examples in problem statements.',
 '3. For construction tasks, reviewed validators check the task rules. Tasks requiring further checker review are excluded from validated Pass@1.',
 '4. APPS cases may be limited and are not necessarily the complete private online judge. Pass@1 here means success on the evaluated APPS test suite.',
 '5. Tests with missing source data, unmatched metadata or checker errors are reported as not evaluated; neither success nor failure is invented.',
 '', '**Raw task-level results:** `APPS_270_Results.csv` and the three participant CSV files.',
 '**Full test suites:** `data/test_cases/person_*/<problem_id>.json` inside `RMT_APPS_Benchmark`.',
 '', '## Cases still requiring manual review', ''])
 flagged=[r for r in rows if r['validation_class']=='REFERENCE_ONLY']
 for r in flagged:
  if r['condition']=='clear':lines.append(f"- {r['person']} / {r['problem_id']}: exact-reference comparison only; multi-output correctness cannot be certified.")
 if not flagged:lines.append('- None identified by current audit flags.')
 (BENCH/'APPS_Report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def create_evidence_archive(summary,rows):
 # Small portable report of all recorded outcomes and source hashes; the
 # original full dataset cases remain in the benchmark directory.
 import zipfile
 target=ROOT/'RMT_APPS_Final_Results.zip'
 with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for name in ['APPS_270_Results.csv','APPS_summary.json','APPS_Report.md','APPS_import_log.json']:
   p=BENCH/name
   if p.is_file():z.write(p,name)
  for person in SOURCES:
   p=BENCH/f'{person}_APPS_results.csv'
   if p.exists():z.write(p,p.name)
   for res in (BENCH/'outputs'/person/'results').glob('*.json'):
    z.write(res,f'raw_verdicts/{person}/{res.name}')
   for source in (BENCH/'data'/'test_cases'/person).glob('*.json'):
    suite=load(source)
    manifest={'problem_id':suite.get('problem_id'),'case_count':len(suite.get('inputs',[])),
        'test_source':suite.get('test_source'),'suite_sha256':suite.get('suite_sha256'),
        'validation_scope':suite.get('validation_scope')}
    z.writestr(f'suite_manifests/{person}/{source.name}',json.dumps(manifest,indent=2,ensure_ascii=False))
 print('Portable report ZIP:',target,flush=True)

def write_summary():
 rows=[]
 for p in SOURCES:
  tasks=load(ROOT/'data'/f'{p}_prompts.json')['tasks']
  for t in tasks:
   pid=str(t['problem_id'])
   suite_path=BENCH/'data'/'test_cases'/p/f'{pid}.json'
   suite=load(suite_path) if suite_path.exists() else {}
   scope=suite.get('validation_scope','missing_source')
   confidence='REFERENCE_ONLY' if 'REQUIRES_REVIEW' in scope else ('BENCHMARK_REFERENCE' if scope=='reference_comparison_unique_output_candidate' else 'TASK_SPECIFIC_VALIDATOR')
   for c in CONDITIONS:
    key=f'{pid}_{c}'
    result_path=BENCH/'outputs'/p/'results'/f'{key}.json'
    result=load(result_path) if result_path.exists() else {}
    full_pass=result.get('pass_at_1')
    passed=(full_pass==1) if full_pass in (0,1) else None
    evaluated=(full_pass in (0,1) and result.get('failure_type')!='checker_error')
    status='EVALUATED' if evaluated else ('JUDGE_OR_CHECKER_ERROR' if result else ('UNAVAILABLE_APPS_CASES' if not suite else 'NOT_EVALUATED'))
    rows.append({
     'person':p,'problem_id':pid,'difficulty_tier':t['difficulty_tier'],'condition':c,
     'status':status,'validation_class':confidence,'validation_scope':scope,
     'case_count':len(suite.get('inputs',[])),'cases_run':result.get('test_cases_executed',''),
     'cases_passed':result.get('test_cases_passed',''),
     'benchmark_checker_pass_all':int(passed) if evaluated else '',
     'pass_at_1_validated':int(passed) if evaluated and confidence!='REFERENCE_ONLY' else '',
     'first_failed_case':result.get('failure_index_1based',''),'failure_type':result.get('failure_type',''),
     'test_source':suite.get('test_source',''),
    })
 output=BENCH/'APPS_270_Results.csv'
 with output.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 counts={}
 for p in SOURCES:
  a=[r for r in rows if r['person']==p];counts[p]={
   'evaluated':sum(r['status']=='EVALUATED' for r in a),
   'validated_pass':sum(r['pass_at_1_validated']==1 for r in a),
   'validated_denominator':sum(r['pass_at_1_validated']!='' for r in a),
   'benchmark_pass':sum(r['benchmark_checker_pass_all']==1 for r in a),
   'benchmark_denominator':sum(r['benchmark_checker_pass_all']!='' for r in a),
  }

 # Separate per-person exports, plus paired condition comparisons by difficulty.
 by_pair={}
 for r in rows:
  by_pair.setdefault((r['person'],r['problem_id']),{})[r['condition']]=r
 paired={}
 for person in SOURCES:
  for tier in ('Introductory','Interview','Competition'):
   both=[]
   for (p,tid),v in by_pair.items():
    if p!=person or len(v)!=2 or v['clear']['difficulty_tier'].lower()!=tier.lower():continue
    if all(x['pass_at_1_validated'] in (0,1) for x in v.values()):
     both.append((v['clear']['pass_at_1_validated'],v['ambiguous']['pass_at_1_validated']))
   both_pass=sum(a==b==1 for a,b in both)
   clear_only=sum(a==1 and b==0 for a,b in both)
   ambiguous_only=sum(a==0 and b==1 for a,b in both)
   both_fail=sum(a==b==0 for a,b in both)
   paired[f'{person}/{tier.lower()}']={
     'fully_validated_pairs':len(both),'both_pass':both_pass,
     'clear_only':clear_only,'ambiguous_only':ambiguous_only,'both_fail':both_fail
   }
  path=BENCH/f'{person}_APPS_results.csv'
  with path.open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(r for r in rows if r['person']==person)

 summary={'created_at_utc':utc(),'source_dataset':REPO_URL,'input_output_provenance':'APPS test split, not public samples, IDs verified against original prompts',
          'results_by_person':counts,'paired_by_tier':paired,
          'interpretation':'Pass@1 validated uses authentic APPS cases with reference-output comparison or reviewed semantic/numeric validators. Reference-only multi-output cases are excluded from validated column. APPS test suites are not necessarily exhaustive hidden official judge cases.',
          'rows':len(rows)}
 dump(BENCH/'APPS_summary.json',summary)
 write_markdown_report(summary,rows)
 create_evidence_archive(summary,rows)
 print('CSV:',output,flush=True)
 print('Summary:',json.dumps(counts,ensure_ascii=False),flush=True)
 return rows

def main():
 parser=argparse.ArgumentParser(description='Reproducible APPS dataset tests for 270 existing RMT Final solutions; no OpenAI calls')
 parser.add_argument('--phase',choices=('all','download','evaluate','summary'),default='all')
 parser.add_argument('--download-workers',type=int,default=3)
 parser.add_argument('--eval-workers',type=int,default=2)
 parser.add_argument('--limit',type=int,default=135)
 args=parser.parse_args()
 if not 1<=args.download_workers<=4 or not 1<=args.eval_workers<=3 or not 1<=args.limit<=135:parser.error('invalid worker count or limit')
 prepare_bench()
 if args.phase in ('all','download'):download_phase(args.download_workers,args.limit)
 if args.phase in ('all','evaluate'):evaluation_phase(args.eval_workers,args.limit)
 if args.phase in ('summary','download'):write_summary()
 print('No API model generations performed. Original outputs/results remain intact.',flush=True)

if __name__=='__main__':main()
