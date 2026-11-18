import sys
import math
import random


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        a %= n
        if not a:
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
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    root = math.isqrt(n)
    if root * root == n:
        return root

    while True:
        y = random.randrange(1, n)
        c = random.randrange(1, n)
        g = 1
        r = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                q = 1
                for _ in range(min(128, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += 128
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


def factor(n):
    result = {}
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p

    stack = [n] if n > 1 else []
    while stack:
        v = stack.pop()
        if is_prime(v):
            result[v] = result.get(v, 0) + 1
        else:
            d = pollard_rho(v)
            stack.append(d)
            stack.append(v // d)
    return result


def main():
    m, x = map(int, sys.stdin.buffer.read().split())
    if x == 1:
        print(m)
        return

    groups = []
    for p, exponent in factor(m).items():
        order = p - 1
        for q in factor(p - 1):
            while order % q == 0 and pow(x, order // q, p) == 1:
                order //= q

        choices = [(1, 1)]
        modulus = p
        phi = p - 1
        choices.append((phi, order))
        for _ in range(1, exponent):
            modulus *= p
            phi *= p
            if pow(x, order, modulus) != 1:
                order *= p
            choices.append((phi, order))
        groups.append(choices)

    states = [(1, 1)]
    for choices in groups:
        next_states = []
        for phi, order in states:
            for local_phi, local_order in choices:
                new_order = order // math.gcd(order, local_order) * local_order
                next_states.append((phi * local_phi, new_order))
        states = next_states

    print(sum(phi // order for phi, order in states))


if __name__ == "__main__":
    main()
