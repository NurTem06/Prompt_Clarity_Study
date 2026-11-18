"""Run INSIDE a network-disabled Docker container, never on the host.

Usage: python -I -B inside_judge_final.py CODE TEST_JSON PERSON TASK_ID TIMEOUT
Checker behavior is explicit: no assumptions about alternative valid outputs.
"""
from __future__ import annotations

import ast
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import time


def numeric_compare(expected: str, actual: str, abs_tol: float, rel_tol: float):
    e=expected.split(); a=actual.split()
    if len(e)!=len(a):return False,'wrong numeric token count'
    try:
        x=list(map(float,e));y=list(map(float,a))
    except ValueError:return False,'non-numeric token'
    ok=all(math.isfinite(aa) and math.isfinite(xx) and
           math.isclose(xx,aa,abs_tol=abs_tol,rel_tol=rel_tol)
           for xx,aa in zip(x,y))
    return ok, '' if ok else 'numeric values outside specified tolerance'


def load_semantic_checker(person: str, task_id: str):
    checkerfile=Path('/work/data/checkers')/f'{person}_{task_id}.py'
    if not checkerfile.exists():
        raise FileNotFoundError(f'No semantic checker: {checkerfile}')
    spec=importlib.util.spec_from_file_location(f'checker_{person}_{task_id}',checkerfile)
    if spec is None or spec.loader is None:
        raise ValueError('Checker could not be loaded')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    func=getattr(module,'validate',None)
    if not callable(func):raise ValueError('Custom checker must define validate(input, expected, actual)')
    return func


def test_program(code_path: Path, testsfile: Path, person: str, task_id: str, timeout: float):
    tests=json.loads(testsfile.read_text(encoding='utf-8'))
    if (str(tests['problem_id'])!=task_id or tests.get('review_status')!='approved'
        or len(tests['inputs']) != len(tests['outputs']) or not tests['inputs']):
        raise ValueError('Only matching nonempty approved suites may be evaluated')
    checker=tests['checker']
    if checker not in ('reference_tokens','numeric_tolerance','semantic'):
        raise ValueError('Approved checker type is required')
    validate=load_semantic_checker(person,task_id) if checker=='semantic' else None
    t0=time.monotonic()
    result={'problem_id':task_id,'total_test_cases':len(tests['inputs']),
            'test_cases_executed':0,'test_cases_passed':0,
            'passed_before_first_failure':0,'pass_at_1':0,'failure_type':None,
            'failure_index_1based':None,'detail':'', 'checker':checker,'syntax_ok':False}
    try:
        ast.parse(code_path.read_text(encoding='utf-8'))
    except SyntaxError as exc:
        result.update(failure_type='syntax_error',detail=f'{exc.msg} (line {exc.lineno})')
        result['runtime_seconds']=round(time.monotonic()-t0,4)
        return result
    result['syntax_ok']=True
    for idx,(inp,ref) in enumerate(zip(tests['inputs'],tests['outputs']),start=1):
        result['test_cases_executed']+=1
        try:
            p=subprocess.run([sys.executable,'-I','-B',str(code_path)],input=inp,
                             text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                             timeout=timeout,cwd='/tmp',check=False)
        except subprocess.TimeoutExpired:
            result.update(failure_type='timeout',failure_index_1based=idx,detail=f'{timeout} seconds per case')
            break
        except Exception as ex:
            result.update(failure_type='runtime_error',failure_index_1based=idx,detail=f'{type(ex).__name__}: {str(ex)[:200]}')
            break
        if p.returncode:
            result.update(failure_type='runtime_error',failure_index_1based=idx,detail=p.stderr[-300:])
            break
        try:
            if checker=='reference_tokens':
                valid=(p.stdout.split()==ref.split())
                reason='' if valid else 'output differs from reference tokens'
            elif checker=='numeric_tolerance':
                valid,reason=numeric_compare(ref,p.stdout,tests['abs_tol'],tests['rel_tol'])
            else:
                valid,reason=validate(inp,ref,p.stdout)
                if not isinstance(valid,bool):raise TypeError('Checker must return bool')
        except Exception as ex:
            result.update(pass_at_1=None,failure_type='checker_error',failure_index_1based=idx,detail=f'{type(ex).__name__}: {str(ex)[:200]}')
            break
        if not valid:
            result.update(failure_type='wrong_answer',failure_index_1based=idx,detail=str(reason)[:300])
            break
        result['test_cases_passed']+=1
        result['passed_before_first_failure']+=1
    else:
        result['pass_at_1']=1
    result['runtime_seconds']=round(time.monotonic()-t0,4)
    return result


if __name__=='__main__':
    if len(sys.argv)!=6:
        raise SystemExit('Expected CODE TEST_JSON PERSON TASK_ID TIMEOUT')
    output=test_program(Path(sys.argv[1]),Path(sys.argv[2]),sys.argv[3],sys.argv[4],float(sys.argv[5]))
    print(json.dumps(output,ensure_ascii=False))
