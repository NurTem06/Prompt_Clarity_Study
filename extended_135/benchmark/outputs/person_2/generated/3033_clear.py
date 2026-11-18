import sys
from bisect import bisect_left, bisect_right
from functools import lru_cache
from math import isqrt


def main():
    B, N = map(int, sys.stdin.buffer.read().split())

    if N < B:
        print(N)
        return

    remaining = N
    factors = []
    p = 2
    while p < B and p * p <= remaining:
        if remaining % p == 0:
            exponent = 0
            while remaining % p == 0:
                remaining //= p
                exponent += 1
            factors.append((p, exponent))
        p = 3 if p == 2 else p + 2

    if remaining > 1:
        if remaining >= B:
            print("impossible")
            return
        factors.append((remaining, 1))

    digits = [1]
    for prime, exponent in factors:
        old = digits[:]
        power = 1
        for _ in range(exponent):
            power *= prime
            if power >= B:
                break
            for value in old:
                product = value * power
                if product < B:
                    digits.append(product)

    digits.sort()
    digits = digits[1:]
    largest = digits[-1]

    limit = (1 << 63) - 1
    max_length = 0
    value = limit
    while value:
        max_length += 1
        value //= B
    max_length = min(max_length, sum(e for _, e in factors))

    powers = [1]
    for _ in range(max_length):
        powers.append(powers[-1] * largest)

    @lru_cache(maxsize=None)
    def solve(n, length):
        if length == 1:
            return (n,) if 2 <= n < B else None

        if n > powers[length] or n < (1 << length):
            return None

        lower = (n + powers[length - 1] - 1) // powers[length - 1]
        lo = bisect_left(digits, max(2, lower))

        if length == 2:
            hi = bisect_right(digits, isqrt(n))
            for i in range(lo, hi):
                d = digits[i]
                if n % d == 0:
                    other = n // d
                    if other < B:
                        return (d, other)
            return None

        root = int(n ** (1.0 / length))
        while (root + 1) ** length <= n:
            root += 1
        while root ** length > n:
            root -= 1

        hi = bisect_right(digits, root)
        for i in range(lo, hi):
            d = digits[i]
            if n % d == 0:
                suffix = solve(n // d, length - 1)
                if suffix is not None:
                    return (d,) + suffix
        return None

    minimum_length = 1
    while minimum_length <= max_length and powers[minimum_length] < N:
        minimum_length += 1

    for length in range(minimum_length, max_length + 1):
        result = solve(N, length)
        if result is not None:
            answer = 0
            for digit in result:
                answer = answer * B + digit
            print(answer if answer <= limit else "impossible")
            return

    print("impossible")


if __name__ == "__main__":
    main()
