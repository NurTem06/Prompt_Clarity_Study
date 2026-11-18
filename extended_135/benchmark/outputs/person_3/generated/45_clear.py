import sys
from math import isqrt

def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    minimum_sum = k * (k + 1) // 2
    if minimum_sum > n:
        print(-1)
        return

    limit = n // minimum_sum
    best = 1
    for divisor in range(1, min(isqrt(n), limit) + 1):
        if n % divisor == 0:
            best = max(best, divisor)
            other = n // divisor
            if other <= limit:
                best = max(best, other)

    answer = [str(best * i) for i in range(1, k)]
    answer.append(str(n - best * k * (k - 1) // 2))
    sys.stdout.write(" ".join(answer) + "\n")

if __name__ == "__main__":
    main()