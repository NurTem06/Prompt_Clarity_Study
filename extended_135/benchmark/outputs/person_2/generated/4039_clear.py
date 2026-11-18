import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
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
    negative.sort(key=lambda project: project[0] + project[1], reverse=True)

    for a, b in positive + negative:
        if rating < a:
            print("NO")
            return
        rating += b

    print("YES")


if __name__ == "__main__":
    main()