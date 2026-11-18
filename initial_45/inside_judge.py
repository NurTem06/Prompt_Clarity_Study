"""RUN ONLY INSIDE A RESTRICTED DOCKER CONTAINER.

This validator compares output against the supplied APPS-style tests. Several
non-unique-output tasks use semantic checkers to avoid false negatives.
"""
import ast
from collections import Counter, deque
import json
import math
from pathlib import Path
import subprocess
import sys


def validate_output(task_id, input_text, reference, candidate):
    """Return (valid, explanation), with conservative problem-specific checks."""
    out = candidate.split()
    exp = str(reference).split()
    try:
        if task_id == 4008:  # Coloring with any valid k-color assignment
            inp = list(map(int, input_text.split()))
            n, k = inp[:2]; values = inp[2:2+n]
            if exp == ['NO']:
                return (out == ['NO'], 'expected NO' if out != ['NO'] else '')
            if not out or out[0] != 'YES' or len(out) != n + 1:
                return False, 'expected YES followed by n colors'
            colors = list(map(int, out[1:]))
            if any(not 1 <= c <= k for c in colors):
                return False, 'color outside allowed range'
            if len(set(colors)) != k:
                return False, 'not all k colors used'
            seen = [set() for _ in range(k+1)]
            for val, color in zip(values, colors):
                if val in seen[color]:
                    return False, 'repeated array value in one color'
                seen[color].add(val)
            return True, ''
        if task_id == 4014:  # Any valid exam preparation schedule
            inp = list(map(int, input_text.split()))
            n, m = inp[:2]
            exams = [tuple(inp[2+3*j:5+3*j]) for j in range(m)]
            if exp == ['-1']:
                return (out == ['-1'], 'expected impossible (-1)' if out != ['-1'] else '')
            if len(out) != n:
                return False, 'expected schedule with n day labels'
            schedule = list(map(int, out))
            if any(not 0 <= label <= m+1 for label in schedule):
                return False, 'invalid activity label'
            exam_days = {d for _, d, _ in exams}
            for day, activity in enumerate(schedule, 1):
                if day in exam_days:
                    if activity != m+1:
                        return False, 'exam day not marked as exam'
                elif activity == m+1:
                    return False, 'non-exam day marked as exam'
                elif activity != 0:
                    s, d, c = exams[activity-1]
                    if not s <= day < d:
                        return False, 'preparation outside allowed window'
            for i, (_, _, c) in enumerate(exams, 1):
                if schedule.count(i) != c:
                    return False, 'wrong number of preparation days'
            return True, ''
        if task_id == 3014:  # Any <= floor(m/2) removed edges leaving a DAG
            inp = list(map(int, input_text.split()))
            n, m = inp[:2]
            if not out:
                return False, 'missing number of removed edges'
            r = int(out[0])
            if r < 0 or r > m//2 or len(out) != r+1:
                return False, 'invalid removal count or output length'
            removed = list(map(int, out[1:]))
            if len(set(removed)) != r or any(not 1 <= index <= m for index in removed):
                return False, 'duplicate or invalid edge index'
            rem = set(removed)
            edges = inp[2:2+2*m]
            adj = [[] for _ in range(n+1)]
            indegree = [0]*(n+1)
            for index in range(1, m+1):
                if index in rem:
                    continue
                u, v = edges[2*(index-1):2*index]
                adj[u].append(v)
                indegree[v] += 1
            queue = deque(i for i in range(1,n+1) if indegree[i] == 0)
            visited = 0
            while queue:
                u = queue.popleft()
                visited += 1
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0: queue.append(v)
            return (visited == n, 'removed edges leave a directed cycle' if visited != n else '')
        if task_id == 4001:   # Divisor list reconstruction, answer not unique in order
            if len(out) != 2:
                return False, 'expected exactly two integers'
            x, y = map(int, out)
            if x <= 0 or y <= 0:
                return False, 'numbers must be positive'
            data = list(map(int, input_text.split()))
            wanted = Counter(data[1:1+data[0]])
            divs = Counter()
            for v in (x, y):
                for d in range(1, math.isqrt(v)+1):
                    if v % d == 0:
                        divs[d] += 1
                        if d*d != v: divs[v//d] += 1
            return (divs == wanted, 'incorrect divisor multiset' if divs != wanted else '')
        if task_id == 4007:  # Assignment of gifts, arbitrary valid permutation
            inp = list(map(int, input_text.split()))
            n = inp[0]; prior = inp[1:1+n]
            if len(out) != n: return False, 'expected n recipients'
            ans = list(map(int, out))
            ok = sorted(ans) == list(range(1,n+1)) and all(ans[i] != i+1 and (prior[i]==0 or prior[i]==ans[i]) for i in range(n))
            return (ok, 'invalid gift permutation' if not ok else '')
        if task_id == 13:    # Topological prerequisite order of minimum closure
            if exp == ['-1']:
                return (out==['-1'],'expected -1' if out != ['-1'] else '')
            if not out or out == ['-1']: return False, 'solution order missing'
            inp = list(map(int,input_text.split()))
            n,k=inp[0:2]; mains=set(inp[2:2+k]); at=2+k
            deps=[[] for _ in range(n+1)]
            for i in range(1,n+1):
                count=inp[at]; at+=1; deps[i]=inp[at:at+count];at+=count
            m=int(out[0]); order=list(map(int,out[1:]))
            if m!=int(exp[0]) or len(order)!=m or len(set(order))!=m or any(not 1<=c<=n for c in order):
                return False,'wrong count, duplicates or invalid course id'
            seen=set()
            for c in order:
                if not set(deps[c]).issubset(seen):return False,'prerequisite appears after course'
                seen.add(c)
            return (mains.issubset(seen),'missing required main courses' if not mains.issubset(seen) else '')
        if task_id == 4000:  # Any three distinct endpoints whose union attains optimum
            if len(out)!=4:return False,'expected best length and three vertices'
            best,a,b,c=map(int,out)
            inp=list(map(int,input_text.split())); n=inp[0]
            if best!=int(exp[0]) or len({a,b,c})!=3 or any(not 1<=v<=n for v in (a,b,c)):
                return False,'invalid optimum or endpoints'
            edges=inp[1:]; adj=[[] for _ in range(n+1)]
            for u,v in zip(edges[::2],edges[1::2]):adj[u].append(v);adj[v].append(u)
            def distances(start):
                ds=[-1]*(n+1);ds[start]=0; queue=deque([start])
                while queue:
                    u=queue.popleft()
                    for v in adj[u]:
                        if ds[v]==-1:ds[v]=ds[u]+1;queue.append(v)
                return ds
            da=distances(a);db=distances(b)
            union=(da[b]+da[c]+db[c])//2
            return (union==best,'three selected vertices do not attain optimum' if union!=best else '')
        if task_id == 4003:  # Any optimal valid L/R sequence
            if len(out)!=2:return False,'expected length and L/R sequence'
            k=int(out[0]); moves=out[1].upper()
            inp=list(map(int,input_text.split())); vals=inp[1:1+inp[0]]
            if k!=int(exp[0]) or len(moves)!=k or any(m not in 'LR' for m in moves):
                return False,'incorrect maximum length or movement sequence'
            l=0;r=len(vals)-1;prev=-1
            for m in moves:
                if l>r:return False,'too many moves'
                if m=='L':v=vals[l];l+=1
                else:v=vals[r];r-=1
                if v<=prev:return False,'chosen values are not strictly increasing'
                prev=v
            return True,''
        if task_id == 4012:  # Any optimum feasible triples
            inp=list(map(int,input_text.split())); t=inp[0]
            if len(out)!=4*t or len(exp)!=4*t:
                return False,'expected 4 output tokens per case'
            got=list(map(int,out));ref=list(map(int,exp));src=inp[1:]
            for j in range(t):
                a,b,c=src[3*j:3*j+3]; res,A,B,C=got[4*j:4*j+4]
                if res!=ref[4*j] or min(A,B,C)<=0 or not(A<=B<=C) or B%A!=0 or C%B!=0:
                    return False,f'invalid optimum or triple in case {j+1}'
                if abs(a-A)+abs(b-B)+abs(c-C)!=res:
                    return False,f'wrong operation count in case {j+1}'
            return True,''
        if task_id == 3013:  # Reference-coordinate tolerance, provisional checker only
            if len(out)!=2 or len(exp)!=2:return False,'expected two coordinates'
            got=list(map(float,out));ans=list(map(float,exp))
            if all(math.isfinite(v) and math.isclose(v,w,rel_tol=1e-5,abs_tol=1e-5) for v,w in zip(got,ans)):
                return True,''
            return False,'coordinates differ from reference beyond tolerance (independent semantic checker recommended)'
        return (out==exp,'output tokens differ from reference' if out!=exp else '')
    except (ValueError,IndexError,OverflowError,ZeroDivisionError,MemoryError) as exc:
        return False,'invalid output format: '+str(exc)[:180]


def test_program(code_path, data_path):
    task=json.loads(Path(data_path).read_text(encoding='utf-8'))
    tests=task['test_cases']
    if not tests or len(tests['inputs'])!=len(tests['outputs']) or not tests['inputs']:
        raise ValueError('No complete test set for task')
    result={'problem_id':task['problem_id'],'total_test_cases':len(tests['inputs']),
            'passed_before_first_failure':0,'pass_at_1':0,'failure_type':None,
            'failure_index_1based':None,'detail':None,
            'checker': 'semantic' if task['problem_id'] in (4000,4001,4003,4007,4012,13) else ('float_reference_provisional' if task['problem_id']==3013 else 'reference_tokens')}
    source=Path(code_path).read_text(encoding='utf-8')
    try:ast.parse(source)
    except SyntaxError as exc:
        result.update(failure_type='syntax_error',detail=f'{exc.msg} (line {exc.lineno})')
        return result
    for idx,(inp,exp) in enumerate(zip(tests['inputs'],tests['outputs']),start=1):
        try:
            cp=subprocess.run([sys.executable,'-I','-B',str(code_path)],input=inp,text=True,
                              stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=10,
                              cwd='/tmp',check=False)
        except subprocess.TimeoutExpired:
            result.update(failure_type='timeout',failure_index_1based=idx,detail='10s per case')
            return result
        except Exception as exc:
            result.update(failure_type='runtime_error',failure_index_1based=idx,detail=str(exc)[:300])
            return result
        if cp.returncode!=0:
            result.update(failure_type='runtime_error',failure_index_1based=idx,detail=cp.stderr[-300:])
            return result
        valid,reason=validate_output(task['problem_id'],inp,exp,cp.stdout)
        if not valid:
            result.update(failure_type='wrong_answer',failure_index_1based=idx,detail=reason[:300])
            return result
        result['passed_before_first_failure']+=1
    result['pass_at_1']=1
    return result

if __name__=='__main__':
    print(json.dumps(test_program(sys.argv[1],sys.argv[2]),ensure_ascii=False))
