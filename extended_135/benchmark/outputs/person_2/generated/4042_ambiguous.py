import sys
import math

x = sys.stdin.read().strip()

for a in range(1, 11):
    for h in range(1, 11):
        r = a * h / math.sqrt(a * a + 4 * h * h)
        if f"{r:.6f}" == x:
            print(a, h)
            sys.exit(0)