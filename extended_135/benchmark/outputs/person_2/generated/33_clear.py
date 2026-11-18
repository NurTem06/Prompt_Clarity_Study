import sys


def main():
    a1, b1, a2, b2, left, right = map(int, sys.stdin.buffer.read().split())
    left = max(left, b1, b2)

    if left > right:
        print(0)
        return

    a, b = a1, a2
    s0, s1 = 1, 0
    while b:
        q = a // b
        a, b = b, a - q * b
        s0, s1 = s1, s0 - q * s1

    g = a
    difference = b2 - b1
    if difference % g:
        print(0)
        return

    modulus = a2 // g
    k = (difference // g * s0) % modulus
    solution = b1 + a1 * k
    period = a1 * modulus

    answer = (right - solution) // period - (left - 1 - solution) // period
    print(answer)


if __name__ == "__main__":
    main()