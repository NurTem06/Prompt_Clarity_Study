import sys

n, a, b, c = map(int, sys.stdin.buffer.read().split())
total = a + b + c
print(min(total, 2 * (total - max(a, b, c)) + n))