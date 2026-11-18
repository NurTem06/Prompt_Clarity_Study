import sys
from math import gcd

def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(values)
    g = 0
    for _ in range(n):
        g = gcd(g, next(values))
        if g == 1:
            print(1)
            return

    answer = 1
    exponent = 0
    while g % 2 == 0:
        g //= 2
        exponent += 1
    answer *= exponent + 1

    p = 3
    while p * p <= g:
        if g % p == 0:
            exponent = 0
            while g % p == 0:
                g //= p
                exponent += 1
            answer *= exponent + 1
        p += 2

    if g > 1:
        answer *= 2

    print(answer)

if __name__ == "__main__":
    main()