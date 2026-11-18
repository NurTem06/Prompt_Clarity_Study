import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    d, n, m = data[:3]
    min_x = [0] * (n + 1)
    max_x = [0] * (n + 1)
    min_y = [0] * (m + 1)
    max_y = [0] * (m + 1)

    end = 3 + 4 * d
    for p in range(3, end, 4):
        x1, y1, x2, y2 = data[p:p + 4]
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        data[p:p + 4] = x1, y1, x2, y2
        min_x[x1] += 1
        max_x[x2] += 1
        min_y[y1] += 1
        max_y[y2] += 1

    for i in range(1, n + 1):
        min_x[i] += min_x[i - 1]
        max_x[i] += max_x[i - 1]

    for i in range(1, m + 1):
        min_y[i] += min_y[i - 1]
        max_y[i] += max_y[i - 1]

    left, right, top, bottom = data[end:end + 4]

    for p in range(3, end, 4):
        x1, y1, x2, y2 = data[p:p + 4]
        horizontal = int(x1 != x2)
        vertical = int(y1 != y2)

        if min_x[x2 - 1] - horizontal != left:
            continue
        if d - max_x[x1] - horizontal != right:
            continue
        if min_y[y2 - 1] - vertical != top:
            continue
        if d - max_y[y1] - vertical != bottom:
            continue

        print((p - 3) // 4 + 1)
        return

    print(-1)


if __name__ == "__main__":
    main()
