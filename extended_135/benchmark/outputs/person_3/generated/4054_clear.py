import sys

a = list(map(int, sys.stdin.buffer.read().split()))
print(min(x // r for x, r in zip(a, (1, 1, 2, 7, 4))))
