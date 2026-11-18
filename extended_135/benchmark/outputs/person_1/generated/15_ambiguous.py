import sys

a, b, c = map(int, sys.stdin.buffer.read().split())
d = b - a

if c == 0:
    print("YES" if d == 0 else "NO")
else:
    print("YES" if d % c == 0 and d // c >= 0 else "NO")