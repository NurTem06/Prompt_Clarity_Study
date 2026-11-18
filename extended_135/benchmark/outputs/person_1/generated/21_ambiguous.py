import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:]
p = a.index(1)
q = a.index(n)
print(max(p, q, n - 1 - p, n - 1 - q))