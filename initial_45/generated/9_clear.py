import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    d, n, m = data[0:3]
    min_x_counts = [0] * (n + 1)
    max_x_counts = [0] * (n + 1)
    min_y_counts = [0] * (m + 1)
    max_y_counts = [0] * (m + 1)
    sofas = []

    pos = 3
    for _ in range(d):
        x1, y1, x2, y2 = data[pos:pos + 4]
        pos += 4

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        sofas.append((x1, y1, x2, y2))
        min_x_counts[x1] += 1
        max_x_counts[x2] += 1
        min_y_counts[y1] += 1
        max_y_counts[y2] += 1

    left, right, top, bottom = data[pos:pos + 4]

    for i in range(1, n + 1):
        min_x_counts[i] += min_x_counts[i - 1]
        max_x_counts[i] += max_x_counts[i - 1]

    for i in range(1, m + 1):
        min_y_counts[i] += min_y_counts[i - 1]
        max_y_counts[i] += max_y_counts[i - 1]

    for index, (x1, y1, x2, y2) in enumerate(sofas, 1):
        spans_x = int(x1 != x2)
        spans_y = int(y1 != y2)

        if min_x_counts[x2 - 1] - spans_x != left:
            continue
        if d - max_x_counts[x1] - spans_x != right:
            continue
        if min_y_counts[y2 - 1] - spans_y != top:
            continue
        if d - max_y_counts[y1] - spans_y != bottom:
            continue

        print(index)
        return

    print(-1)


if __name__ == "__main__":
    main()