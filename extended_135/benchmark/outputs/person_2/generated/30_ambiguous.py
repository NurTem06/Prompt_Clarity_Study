import sys
import math
import random

SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime(n):
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p

    d = n - 1
    s = (d & -d).bit_length() - 1
    d >>= s

    for a in MR_BASES:
        a %= n
        if a == 0:
            continue
        v = pow(a, d, n)
        if v == 1 or v == n - 1:
            continue
        for _ in range(s - 1):
            v = v * v % n
            if v == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n):
    for p in SMALL_PRIMES:
        if n % p == 0:
            return p

    while True:
        y = random.randrange(1, n)
        c = random.randrange(1, n)
        r = 1
        g = 1

        while g == 1:
            z = y
            for _ in range(r):
                y = (y * y + c) % n

            k = 0
            while k < r and g == 1:
                saved_y = y
                q = 1
                block = min(128, r - k)
                for _ in range(block):
                    y = (y * y + c) % n
                    q = q * abs(z - y) % n
                g = math.gcd(q, n)
                k += block
            r <<= 1

        if g == n:
            while True:
                saved_y = (saved_y * saved_y + c) % n
                g = math.gcd(abs(z - saved_y), n)
                if g > 1:
                    break

        if g != n:
            return g


def factorize(n):
    factors = {}

    for p in SMALL_PRIMES:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p

    stack = [n] if n > 1 else []
    while stack:
        v = stack.pop()
        if is_prime(v):
            factors[v] = factors.get(v, 0) + 1
        else:
            d = pollard_rho(v)
            stack.append(d)
            stack.append(v // d)

    return factors


def main():
    m, x = map(int, sys.stdin.buffer.read().split())
    if x == 1:
        print(m)
        return

    groups = []
    for p, exponent in factorize(m).items():
        order = p - 1
        if x % p == 1:
            order = 1
        else:
            for q in factorize(p - 1):
                while order % q == 0 and pow(x, order // q, p) == 1:
                    order //= q

        choices = [(1, 1)]
        modulus = p
        phi = p - 1

        for k in range(1, exponent + 1):
            if k > 1:
                modulus *= p
                phi *= p
                if pow(x, order, modulus) != 1:
                    order *= p
            choices.append((phi, order))

        groups.append(choices)

    def count(index, phi, order):
        if index == len(groups):
            return phi // order

        total = 0
        for next_phi, next_order in groups[index]:
            combined_order = order // math.gcd(order, next_order) * next_order
            total += count(index + 1, phi * next_phi, combined_order)
        return total

    print(count(0, 1, 1))


if __name__ == "__main__":
    main()