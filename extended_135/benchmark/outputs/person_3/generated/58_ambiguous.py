import sys

def main():
    n, a, b = map(int, sys.stdin.buffer.read().split())

    patterns = [
        (x, y)
        for x in range(5)
        for y in range(3)
        if (x or y) and x * a + y * b <= n
    ]

    dp = [[7] * 3 for _ in range(5)]
    dp[0][0] = 0

    for i in range(5):
        for j in range(3):
            for x, y in patterns:
                if i + x <= 4 and j + y <= 2:
                    dp[i + x][j + y] = min(
                        dp[i + x][j + y], dp[i][j] + 1
                    )

    print(dp[4][2])

if __name__ == "__main__":
    main()
