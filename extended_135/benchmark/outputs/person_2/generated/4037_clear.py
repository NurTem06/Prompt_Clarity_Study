import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, rating = data[0], data[1]
    positive = []
    negative = []

    for i in range(n):
        a, b = data[2 + 2 * i:4 + 2 * i]
        if b >= 0:
            positive.append((a, b))
        else:
            negative.append((max(a, -b), b))

    positive.sort()
    completed = 0

    for a, b in positive:
        if rating < a:
            break
        rating += b
        completed += 1

    negative.sort(key=lambda project: project[0] + project[1], reverse=True)

    dp = [-1] * (len(negative) + 1)
    dp[0] = rating

    for i, (a, b) in enumerate(negative):
        for count in range(i, -1, -1):
            if dp[count] >= a:
                dp[count + 1] = max(dp[count + 1], dp[count] + b)

    best = max(count for count, remaining in enumerate(dp) if remaining >= 0)
    print(completed + best)


if __name__ == "__main__":
    main()