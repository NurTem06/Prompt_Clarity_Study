import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    dp = [0] * (n + 1)
    dp[0] = 1
    last = [None] * 26

    for i, c in enumerate(s):
        idx = c - 97
        previous = last[idx]
        new_dp = dp.copy()

        if previous is None:
            for length in range(1, i + 2):
                new_dp[length] += dp[length - 1]
        else:
            for length in range(1, i + 2):
                new_dp[length] += dp[length - 1] - previous[length - 1]

        last[idx] = dp
        dp = new_dp

    answer = 0
    for length in range(n, -1, -1):
        take = min(k, dp[length])
        answer += take * (n - length)
        k -= take
        if k == 0:
            print(answer)
            return

    print(-1)


if __name__ == "__main__":
    main()