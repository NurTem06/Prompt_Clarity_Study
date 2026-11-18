import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = map(int, data[:2])
    s = data[2]

    dp = [0] * (n + 1)
    dp[0] = 1
    last = {}

    for i, ch in enumerate(s, 1):
        old = dp
        previous = last.get(ch)
        dp = old.copy()

        for length in range(1, i + 1):
            dp[length] += old[length - 1]
            if previous is not None:
                dp[length] -= previous[length - 1]

        last[ch] = old

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