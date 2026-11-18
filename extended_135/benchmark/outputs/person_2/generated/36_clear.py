import sys
from math import isqrt

n = int(sys.stdin.buffer.read())
k = (isqrt(12 * n + 9) - 3) // 6
if 3 * k * (k + 1) < n:
    k += 1

remaining = n - 3 * k * (k - 1)
x, y = 2 * k, 0

for dx, dy in ((-1, 2), (-2, 0), (-1, -2),
               (1, -2), (2, 0), (1, 2)):
    steps = min(remaining, k)
    x += dx * steps
    y += dy * steps
    remaining -= steps
    if remaining == 0:
        break

print(x, y)