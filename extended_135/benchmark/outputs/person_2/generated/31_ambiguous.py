import sys

def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    mod = 1_000_003

    if n < 60 and k > (1 << n):
        print(1, 1)
        return

    m = k - 1
    twos = m - m.bit_count()
    denominator = pow(2, (n * m - twos) % (mod - 1), mod)
    days_mod = pow(2, n, mod)

    if m >= days_mod:
        print(denominator, denominator)
        return

    product = 1
    for i in range(1, m + 1):
        product = product * (days_mod - i) % mod

    product = product * pow(2, (-twos) % (mod - 1), mod) % mod
    numerator = (denominator - product) % mod
    print(numerator, denominator)

if __name__ == "__main__":
    main()
