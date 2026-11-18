import sys
from math import isqrt

def main():
    n, m = map(int, sys.stdin.buffer.read().split())
    if n <= m:
        print(n)
        return

    remaining = n - m
    k = (isqrt(8 * remaining + 1) - 1) // 2
    if k * (k + 1) // 2 < remaining:
        k += 1
    print(m + k)

if __name__ == "__main__":
    main()