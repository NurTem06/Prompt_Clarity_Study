import sys
from math import isqrt
from bisect import bisect_right


def main():
    a, b = map(int, sys.stdin.buffer.read().split())
    total = a + b

    limit = isqrt(total)
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'

    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start::p] = b'\x00' * ((limit - start) // p + 1)

    def divisors(value):
        result = [1]
        p = 2
        while p != -1 and p * p <= value:
            if value % p == 0:
                power = 1
                old = result[:]
                while value % p == 0:
                    value //= p
                    power *= p
                    result.extend(d * power for d in old)
            p = sieve.find(b'\x01', p + 1)

        if value > 1:
            result += [d * value for d in result]
        result.sort()
        return result

    da = divisors(a)
    db = divisors(b)
    dn = divisors(total)

    for width in reversed(dn):
        if width > limit:
            continue
        height = total // width

        d = da[bisect_right(da, width) - 1]
        if a // d <= height:
            print(2 * (width + height))
            return

        d = db[bisect_right(db, width) - 1]
        if b // d <= height:
            print(2 * (width + height))
            return


if __name__ == "__main__":
    main()