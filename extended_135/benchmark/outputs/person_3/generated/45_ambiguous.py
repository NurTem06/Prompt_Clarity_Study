import sys
from math import isqrt

def main():
    n, k = map(int, sys.stdin.buffer.read().split())

    minimum = k * (k + 1) // 2
    if minimum > n:
        print(-1)
        return

    if k == 1:
        print(n)
        return

    limit = n // minimum
    best = 1

    for d in range(1, min(isqrt(n), limit) + 1):
        if n % d == 0:
            best = max(best, d)
            other = n // d
            if other <= limit:
                best = max(best, other)

    result = [str(best * i) for i in range(1, k)]
    result.append(str(n - best * k * (k - 1) // 2))
    sys.stdout.write(" ".join(result) + "\n")

if __name__ == "__main__":
    main()