import sys
import math


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    vectors = []
    atan2 = math.atan2

    for i in range(n):
        x = data[2 * i + 1]
        y = data[2 * i + 2]
        vectors.append((atan2(y, x), x, y, i + 1))

    vectors.sort()
    best_cross = best_dot = None
    answer = (1, 2)

    previous = vectors[-1]
    for current in vectors:
        _, x1, y1, i = previous
        _, x2, y2, j = current

        cross = abs(x1 * y2 - y1 * x2)
        dot = x1 * x2 + y1 * y2

        if best_dot is None:
            better = True
        elif (dot >= 0) != (best_dot >= 0):
            better = dot >= 0
        else:
            better = cross * best_dot < best_cross * dot

        if better:
            best_cross = cross
            best_dot = dot
            answer = (i, j)

        previous = current

    print(*answer)


if __name__ == "__main__":
    main()