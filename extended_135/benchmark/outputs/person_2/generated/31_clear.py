import sys

def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    MOD = 1000003

    if n < 60 and k > (1 << n):
        print(1, 1)
        return

    m = k - 1
    valuation = m - bin(m).count("1")
    exponent = n * m - valuation
    denominator = pow(2, exponent, MOD)

    days_mod = pow(2, n, MOD)
    if m >= days_mod:
        noncollision = 0
    else:
        product = 1
        for factor in range(days_mod - m, days_mod):
            product = product * factor % MOD
        noncollision = product * pow((MOD + 1) // 2, valuation, MOD) % MOD

    print((denominator - noncollision) % MOD, denominator)

if __name__ == "__main__":
    main()
