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
    negative.sort(key=lambda project: project[0] + project[1], reverse=True)

    for required, change in positive + negative:
        if rating < required:
            print("NO")
            return
        rating += change

    print("YES")


if __name__ == "__main__":
    main()