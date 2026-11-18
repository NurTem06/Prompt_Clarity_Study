import sys

a, b, c = map(int, sys.stdin.buffer.read().split())
print("Yes" if any((c - a * x) % b == 0 for x in range(c // a + 1)) else "No")