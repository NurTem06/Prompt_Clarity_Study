import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, rating = data[0], data[1]
    positive = []
    negative = []

    for i in range(n):
        a, b = data[2 + 2 * i], data[3 + 2 * i]
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
    best = 0

    for a, b in negative:
        for count in range(best, -1, -1):
            if dp[count] >= a:
                new_rating = dp[count] + b
                if new_rating > dp[count + 1]:
                    dp[count + 1] = new_rating
                    if count + 1 > best:
                        best = count + 1

    print(completed + best)


if __name__ == "__main__":
    main()
