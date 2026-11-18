import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1:n + 1]
    total = sum(values)

    omega = [0] * (total + 1)
    for p in range(2, total + 1):
        if omega[p] == 0:
            for multiple in range(p, total + 1, p):
                omega[multiple] += 1

    size = 1 << n
    sums = [0] * size
    scores = [0] * size
    for i, value in enumerate(values):
        bit = 1 << i
        for mask in range(bit):
            new_mask = bit | mask
            sums[new_mask] = sums[mask] + value
            scores[new_mask] = omega[sums[new_mask]]

    dp = [0] * size
    for mask in range(1, size):
        remainder = mask ^ (mask & -mask)
        best = scores[mask]
        sub = remainder
        while sub:
            candidate = dp[sub] + scores[mask ^ sub]
            if candidate > best:
                best = candidate
            sub = (sub - 1) & remainder
        dp[mask] = best

    print(dp[-1])


if __name__ == "__main__":
    main()