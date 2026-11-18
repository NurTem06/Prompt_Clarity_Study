import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1:n + 1]
    total = sum(values)

    prime_factors = [0] * (total + 1)
    for p in range(2, total + 1):
        if prime_factors[p] == 0:
            for multiple in range(p, total + 1, p):
                prime_factors[multiple] += 1

    size = 1 << n
    sums = [0] * size
    scores = [0] * size
    for mask in range(1, size):
        bit = mask & -mask
        sums[mask] = sums[mask ^ bit] + values[bit.bit_length() - 1]
        scores[mask] = prime_factors[sums[mask]]

    dp = [0] * size
    for mask in range(1, size):
        bit = mask & -mask
        remaining = mask ^ bit
        best = scores[mask]
        subset = remaining
        while True:
            candidate = scores[subset | bit] + dp[remaining ^ subset]
            if candidate > best:
                best = candidate
            if subset == 0:
                break
            subset = (subset - 1) & remaining
        dp[mask] = best

    print(dp[-1])


if __name__ == "__main__":
    main()