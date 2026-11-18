import sys
import math
import random
from bisect import bisect_right


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n):
    for p in (2, 3, 5, 7, 11, 13):
        if n % p == 0:
            return p

    while True:
        c = random.randrange(1, n)
        x = random.randrange(2, n)
        y = x
        d = 1

        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)

        if d != n:
            return d


def factor(n, result):
    if n == 1:
        return
    if is_prime(n):
        result[n] = result.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factor(d, result)
    factor(n // d, result)


def divisors(n):
    factors = {}
    factor(n, factors)
    result = [1]
    for p, exponent in factors.items():
        old = result[:]
        power = 1
        for _ in range(exponent):
            power *= p
            result.extend(d * power for d in old)
    result.sort()
    return result


def main():
    a, b = map(int, sys.stdin.buffer.read().split())
    total = a + b

    da = divisors(a)
    db = da if a == b else divisors(b)
    outer = divisors(total)

    limit = math.isqrt(total)
    index = bisect_right(outer, limit) - 1

    for i in range(index, -1, -1):
        width = outer[i]
        height = total // width

        p = da[bisect_right(da, width) - 1]
        if a // p <= height:
            print(2 * (width + height))
            return

        p = db[bisect_right(db, width) - 1]
        if b // p <= height:
            print(2 * (width + height))
            return


if __name__ == "__main__":
    main()