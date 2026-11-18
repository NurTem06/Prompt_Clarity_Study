import sys


def main():
    s = sys.stdin.buffer.readline().strip()
    n = len(s)

    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        row = lcp[i]
        next_row = lcp[i + 1]
        for j in range(i + 1, n):
            if s[i] == s[j]:
                row[j] = next_row[j + 1] + 1

    divisors = [[] for _ in range(n + 1)]
    for period in range(1, n // 2 + 1):
        for length in range(period * 2, n + 1, period):
            divisors[length].append(period)

    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        row = dp[i]
        row[i + 1] = 1
        for j in range(i + 2, n + 1):
            length = j - i
            best = length

            for period in divisors[length]:
                if lcp[i][i + period] >= length - period:
                    best = min(best, row[i + period])

            if best > 1:
                for k in range(i + 1, j):
                    candidate = row[k] + dp[k][j]
                    if candidate < best:
                        best = candidate
                        if best == 2:
                            break

            row[j] = best

    print(dp[0][n])


if __name__ == "__main__":
    main()