import sys

a, b, c, d = map(int, sys.stdin.buffer.read().split())
print(int(a == d and (a > 0 or c == 0)))
