import sys
from math import gcd

def main():
    a1, b1, a2, b2, left, right = map(int, sys.stdin.buffer.read().split())

    left = max(left, b1, b2)
    g = gcd(a1, a2)
    difference = b2 - b1

    if left > right or difference % g:
        print(0)
        return

    modulus = a2 // g
    if modulus == 1:
        k = 0
    else:
        k = (difference // g) * pow(a1 // g, -1, modulus) % modulus

    first = b1 + a1 * k
    period = a1 * modulus
    print((right - first) // period - (left - 1 - first) // period)

if __name__ == "__main__":
    main()