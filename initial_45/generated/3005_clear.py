import sys


def main():
    s = sys.stdin.buffer.readline().strip()
    n = len(s)
    if not n:
        return

    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        row = lcp[i]
        next_row = lcp[i + 1]
        for j in range(i + 1, n):
            if s[i] == s[j]:
                row[j] = next_row[j + 1] + 1

    divisors = [[] for _ in range(n + 1)]
    for p in range(1, n // 2 + 1):
        for length in range(2 * p, n + 1, p):
            divisors[length].append(p)

    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        row = dp[i]
        row[i + 1] = 1
        for j in range(i + 2, n + 1):
            length = j - i
            best = length

            for p in divisors[length]:
                if lcp[i][i + p] >= length - p:
                    best = min(best, row[i + p])

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
