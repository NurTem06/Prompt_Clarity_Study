import sys

n, k, t = map(int, sys.stdin.buffer.read().split())
print(min(t, k, n + k - t))