import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = map(int, data[:2])
    s = data[2]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    last = {}

    for i, char in enumerate(s, 1):
        dp[i][0] = 1
        previous = last.get(char, 0)
        for length in range(1, i + 1):
            dp[i][length] = dp[i - 1][length] + dp[i - 1][length - 1]
            if previous:
                dp[i][length] -= dp[previous - 1][length - 1]
        last[char] = i

    cost = 0
    for length in range(n, -1, -1):
        take = min(k, dp[n][length])
        cost += take * (n - length)
        k -= take
        if k == 0:
            print(cost)
            return

    print(-1)


if __name__ == "__main__":
    main()