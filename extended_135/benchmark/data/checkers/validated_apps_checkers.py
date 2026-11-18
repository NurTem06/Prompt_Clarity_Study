"""Task-specific validators for APPS tasks with multiple legitimate outputs.

Each validate_<APPS_ID>(input, reference_output, candidate_output) checks the
actual task constraints, not textual similarity. `NO`/`IMPOSSIBLE` cases rely
on the benchmark's supplied reference for the existence decision.
"""
import bisect
import collections
import math
import re


def nums(s):return [int(x) for x in s.split()]
def result(valid,why=''):return bool(valid), ('' if valid else why or 'invalid constructed output')
def impossible(out,ref,word='NO'):
 return result(out.strip()==word and ref.strip()==word,'impossibility claim disagrees with benchmark')


def validate_4017(inp,ref,out):
 try:
  x=nums(inp);n=x[0];a=x[1:]
  if len(a)!=n:return result(False,'invalid input')
  outnums=nums(out);k=outnums[0];chosen=outnums[1:]
  if k!=len(chosen) or len(set(chosen))!=k or any(not 1<=p<=n for p in chosen):return result(False,'invalid index list')
  total=sum(a)
  counts=collections.Counter(a);top=max(a);other=max((v for v in a if v!=top),default=0)
  correct=set()
  for i,v in enumerate(a,1):
   newtop=other if v==top and counts[top]==1 else top
   if 2*newtop==total-v:correct.add(i)
  return result(set(chosen)==correct,'incorrect set of removable indices')
 except Exception as e:return result(False,'malformed answer: '+str(e)[:100])


def validate_4019(inp,ref,out):
 if out.strip().upper()=='NO':return impossible(out,ref)
 try:
  d=nums(inp);n,m,D=d[:3];edges=[(min(d[i],d[i+1]),max(d[i],d[i+1])) for i in range(3,3+2*m,2)]
  tokens=out.split()
  if tokens[0]!='YES':return result(False,'expected YES/NO')
  numsout=list(map(int,tokens[1:]))
  if len(numsout)!=2*(n-1):return result(False,'wrong number of tree edges')
  if sum(1 in (numsout[i],numsout[i+1]) for i in range(0,len(numsout),2))!=D:return result(False,'wrong degree of vertex 1')
  edge_set=set(edges);parent=list(range(n+1))
  def find(z):
   while parent[z]!=z:
    parent[z]=parent[parent[z]];z=parent[z]
   return z
  for u,v in zip(numsout[::2],numsout[1::2]):
   if not (1<=u<=n and 1<=v<=n) or (min(u,v),max(u,v)) not in edge_set:return result(False,'output edge is not in original graph')
   a,b=find(u),find(v)
   if a==b:return result(False,'cycle in spanning tree')
   parent[a]=b
  return result(len({find(i) for i in range(1,n+1)})==1,'disconnected tree')
 except Exception as e:return result(False,'malformed tree: '+str(e)[:100])


def validate_28(inp,ref,out):
 # The optimal operation count is a uniquely determined integer: read it from APPS.
 try:
  lines=inp.strip().splitlines();n=int(lines[0]);rows=[l.split() for l in lines[1:1+n]]
  if len(rows)!=n or any(len(x)!=2 for x in rows):return result(False,'invalid source')
  files={f:f for f,typ in rows};types={f:typ for f,typ in rows}
  z=out.strip().splitlines();k=int(z[0]);want=int(ref.strip().splitlines()[0]);
  if k!=want or len(z)!=k+1:return result(False,'operation count not minimal or lines missing')
  for line in z[1:]:
   tokens=line.split()
   if len(tokens)!=3 or tokens[0]!='move':return result(False,'malformed move command')
   _,src,dest=tokens
   if src not in files or not re.fullmatch('[0-9a-z]{1,6}',dest):return result(False,'invalid source or destination')
   old=files.pop(src);oldtype=types.pop(src)
   files[dest]=old;types[dest]=oldtype  # overwrite allowed by problem statement
  if set(files)!={str(i) for i in range(1,n+1)}:return result(False,'filenames are not 1..n')
  typelist=[types[str(i)] for i in range(1,n+1)]
  return result(typelist==sorted(typelist,reverse=True),'examples must occur before regular tests')
 except Exception as e:return result(False,'malformed move sequence: '+str(e)[:100])


def validate_3028(inp,ref,out):
 if out.strip()=='-1':return impossible(out,ref,word='-1')
 try:
  d=nums(inp);n,m,p=d[:3];board=d[3:]
  if len(board)!=n*m:return result(False,'board data invalid')
  o=nums(out);k=o[0];moves=o[1:]
  if k!=len(moves) or not 0<=k<=p*n*m or any(not 1<=x<=n*m for x in moves):return result(False,'move list invalid')
  # Each move increments every cell in the selected row/column, once at
  # the intersection. Aggregate counts mod p instead of simulating O(k*n*m).
  row=[0]*n;col=[0]*m;intersection=[0]*(n*m)
  for x in moves:
   r,c=divmod(x-1,m);row[r]+=1;col[c]+=1;intersection[x-1]+=1
  for x,v in enumerate(board):
   r,c=divmod(x,m)
   added=row[r]+col[c]-intersection[x]
   if ((v-1+added)%p)+1!=p:return result(False,'board not completely solved')
  return result(True)
 except Exception as e:return result(False,'malformed move list: '+str(e)[:100])


def lds_length(s):
 tails=[]
 for ch in s:
  x=-ord(ch);i=bisect.bisect_left(tails,x)
  if i==len(tails):tails.append(x)
  else:tails[i]=x
 return len(tails)


def validate_4030(inp,ref,out):
 try:
  lines=inp.splitlines();n=int(lines[0]);s=lines[1].strip()
  tokens=out.split();k=int(tokens[0]);c=list(map(int,tokens[1:]))
  if len(c)!=n or not 1<=k<=n or len(set(c))!=k or min(c)!=1 or max(c)!=k:return result(False,'invalid colors')
  prev={}
  for ch,color in zip(s,c):
   if color in prev and ch<prev[color]:return result(False,'same-color sequence must be nondecreasing')
   prev[color]=ch
  return result(k==lds_length(s),'not minimum possible number of colors')
 except Exception as e:return result(False,'malformed coloring: '+str(e)[:100])


def validate_4034(inp,ref,out):
 if out.strip()=='NO':return impossible(out,ref)
 try:
  n,s=inp.splitlines()[:2];n=int(n);s=s.strip()
  parts=out.split();c=parts[1];
  if parts[0]!='YES' or len(c)!=n or set(c)-set('01'):return result(False,'malformed color array')
  for color in '01':
   sub=''.join(ch for ch,group in zip(s,c) if group==color)
   if sub!=''.join(sorted(sub)):return result(False,'same-color sequence not sorted')
  return result(True)
 except Exception as e:return result(False,'malformed answer: '+str(e)[:100])


def validate_4036(inp,ref,out):
 if out.strip()=='NO':return impossible(out,ref)
 try:
  n,k=nums(inp);o=out.split()
  if o[0]!='YES':return result(False,'expected YES/NO')
  arr=list(map(int,o[1:]))
  if len(arr)!=k or sum(arr)!=n:return result(False,'incorrect length or sum')
  return result(all(x>0 and x<y<=2*x for x,y in zip(arr,arr[1:])) and arr[0]>0,'numbers not strictly increasing or exceed doubling constraint')
 except Exception as e:return result(False,'malformed answer: '+str(e)[:100])


def validate_4038(inp,ref,out):
 if out.strip()=='NO':return impossible(out,ref)
 try:
  d=nums(inp);n=d[0];source=collections.Counter(d[1:]);o=out.split()
  if o[0]!='YES':return result(False,'expected YES/NO')
  vals=list(map(int,o[1:]))
  if len(vals)!=n*n or collections.Counter(vals)!=source:return result(False,'multiset not preserved')
  return result(all(vals[i*n+j]==vals[(n-1-i)*n+j]==vals[i*n+n-1-j]
       for i in range(n) for j in range(n)),'matrix not palindromic across both axes')
 except Exception as e:return result(False,'malformed matrix: '+str(e)[:100])


def validate_4042(inp,ref,out):
 try:
  x=inp.strip();a,h=nums(out)
  if not(1<=a<=10 and 1<=h<=10):return result(False,'a,h outside [1,10]')
  radius=a*h/math.sqrt(a*a+4*h*h)
  return result(f'{radius:.6f}'==f'{float(x):.6f}','radius is not target value rounded to 6 decimals')
 except Exception as e:return result(False,'malformed pyramid dimensions: '+str(e)[:100])


def validate_4043(inp,ref,out):
 if out.strip()=='NO':return impossible(out,ref)
 try:
  n,d,k=nums(inp);o=out.split()
  if o[0]!='YES':return result(False,'expected YES/NO')
  ints=list(map(int,o[1:]));
  if len(ints)!=2*(n-1):return result(False,'wrong edge count')
  edges=list(zip(ints[::2],ints[1::2]));adj=[[] for _ in range(n+1)];par=list(range(n+1))
  def find(x):
   while par[x]!=x:
    par[x]=par[par[x]];x=par[x]
   return x
  for a,b in edges:
   if not(1<=a<=n and 1<=b<=n):return result(False,'invalid vertex label')
   aa,bb=find(a),find(b)
   if aa==bb:return result(False,'cycle')
   par[aa]=bb;adj[a].append(b);adj[b].append(a)
  if len({find(i) for i in range(1,n+1)})!=1:return result(False,'disconnected')
  if any(len(adj[i])>k for i in range(1,n+1)):return result(False,'degree greater than k')
  def farthest(start):
   q=collections.deque([start]);dist={start:0};ans=(start,0)
   while q:
    u=q.popleft();ans=(u,dist[u]) if dist[u]>ans[1] else ans
    for v in adj[u]:
     if v not in dist:dist[v]=dist[u]+1;q.append(v)
   return ans
  end,_=farthest(1);diam=farthest(end)[1]
  return result(diam==d,'tree diameter differs from required d')
 except Exception as e:return result(False,'malformed tree: '+str(e)[:100])


def validate_4044(inp,ref,out):
 try:
  a,b,x=nums(inp);s=out.strip()
  return result(len(s)==a+b and s.count('0')==a and s.count('1')==b and
   sum(s[i]!=s[i+1] for i in range(len(s)-1))==x,'binary string has wrong counts/transitions')
 except Exception as e:return result(False,'malformed answer: '+str(e)[:100])


def validate_43(inp,ref,out):
 try:
  a=nums(inp);n=a[0];coords=[(a[2*i+1],a[2*i+2]) for i in range(n)]
  i,j=nums(out);i-=1;j-=1
  if not 0<=i<n or not 0<=j<n or i==j:return result(False,'invalid index pair')
  angles=[math.atan2(y,x)%(2*math.pi) for x,y in coords]
  sorted_angles=sorted(angles)
  best=min((sorted_angles[k+1]-sorted_angles[k] for k in range(n-1)),default=2*math.pi)
  best=min(best,2*math.pi-sorted_angles[-1]+sorted_angles[0])
  diff=abs(angles[i]-angles[j]);angle=min(diff,2*math.pi-diff)
  return result(angle<=best+1e-10,'pair not a minimum non-oriented angle')
 except Exception as e:return result(False,'malformed pair: '+str(e)[:100])


def validate_4045(inp,ref,out):
 if out.strip()=='NO':return impossible(out,ref)
 try:
  lines=inp.splitlines();n=int(lines[0]);forbidden=lines[1].strip(),lines[2].strip();o=out.split()
  if o[0]!='YES' or len(o)!=2:return result(False,'must output YES and a string')
  s=o[1]
  return result(len(s)==3*n and all(s.count(ch)==n for ch in 'abc') and all(x not in s for x in forbidden),'invalid constructed string')
 except Exception as e:return result(False,'malformed string: '+str(e)[:100])


def validate_4050(inp,ref,out):
 try:
  d=nums(inp);n=d[0];arr=d[1:];z=nums(out);k=z[0];pairs=list(zip(z[1::2],z[2::2]))
  if len(pairs)!=k or k<1 or any(not 1<=a<=b<=n for a,b in pairs):return result(False,'invalid intervals')
  pairs.sort()
  if any(pairs[i][1]>=pairs[i+1][0] for i in range(len(pairs)-1)):return result(False,'intervals overlap')
  pref=[0];
  for a in arr:pref.append(pref[-1]+a)
  if len({pref[r]-pref[l-1] for l,r in pairs})!=1:return result(False,'different interval sums')
  # Unique optimum count supplied by APPS reference.
  want=int(ref.split()[0])
  return result(k==want,'number of equal-sum intervals not maximum')
 except Exception as e:return result(False,'malformed interval set: '+str(e)[:100])


def validate_4053(inp,ref,out):
 try:
  lines=inp.strip().splitlines();n=int(lines[0]);pieces=lines[1:];s=out.strip()
  if len(pieces)!=2*n-2 or len(s)!=len(pieces) or set(s)-set('PS') or s.count('P')!=n-1:return result(False,'wrong length or P/S counts')
  long=[p for p in pieces if len(p)==n-1]
  if len(long)!=2:return result(False,'invalid input')
  possible={long[0]+long[1][-1],long[1]+long[0][-1]}
  return result(any(all((candidate.startswith(p) if flag=='P' else candidate.endswith(p))
     for p,flag in zip(pieces,s)) for candidate in possible),'no underlying string consistent with P/S labels')
 except Exception as e:return result(False,'malformed label string: '+str(e)[:100])


def validate_45(inp,ref,out):
 if out.strip()=='-1':return impossible(out,ref,word='-1')
 try:
  n,k=nums(inp);arr=nums(out)
  if len(arr)!=k or sum(arr)!=n or any(x<=0 for x in arr) or any(arr[i]>=arr[i+1] for i in range(k-1)):
   return result(False,'not a strictly increasing positive sequence with required sum')
  gcd=math.gcd(*arr)
  # Max gcd = n / smallest divisor >= k(k+1)/2.
  triangular=k*(k+1)//2
  if triangular>n:return result(False,'sequence impossible')
  best=0
  for x in range(1,math.isqrt(n)+1):
   if n%x:continue
   if x>=triangular:best=max(best,n//x)
   y=n//x
   if y>=triangular:best=max(best,x)
  return result(gcd==best,'GCD not globally maximal')
 except Exception as e:return result(False,'malformed sequence: '+str(e)[:100])


def longest_palindrome(s):
 # Manacher O(n), adequate for N up to 1e6.
 n=len(s);odd=[0]*n;l=r=0;best=0
 for i in range(n):
  k=1 if i>r else min(odd[l+r-i],r-i+1)
  while i-k>=0 and i+k<n and s[i-k]==s[i+k]:k+=1
  odd[i]=k;best=max(best,2*k-1)
  if i+k-1>r:l=i-k+1;r=i+k-1
 even=[0]*n;l=r=0
 for i in range(n):
  k=0 if i>r else min(even[l+r-i+1],r-i+1)
  while i-k-1>=0 and i+k<n and s[i-k-1]==s[i+k]:k+=1
  even[i]=k;best=max(best,2*k)
  if i+k-1>r:l=i-k;r=i+k-1
 return best


def validate_3053(inp,ref,out):
 if out.strip()=='IMPOSSIBLE':return impossible(out,ref,word='IMPOSSIBLE')
 try:
  n,k,p=nums(inp);s=out.strip()
  if len(s)!=n or not s.isascii() or not s.islower() or not s.isalpha() or len(set(s))!=k:
   return result(False,'wrong string length/alphabet/number of distinct letters')
  return result(longest_palindrome(s)==p,'longest palindrome substring length differs')
 except Exception as e:return result(False,'malformed answer: '+str(e)[:100])
