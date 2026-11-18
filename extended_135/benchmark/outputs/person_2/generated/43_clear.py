import sys
import math


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    vectors = [
        (data[2 * i + 1], data[2 * i + 2], i + 1)
        for i in range(n)
    ]
    vectors.sort(key=lambda v: math.atan2(v[1], v[0]))

    best_cross = best_dot = None
    answer_a = answer_b = 0
    previous = vectors[-1]

    for current in vectors:
        x1, y1, i = previous
        x2, y2, j = current
        cross = abs(x1 * y2 - y1 * x2)
        dot = x1 * x2 + y1 * y2

        if best_dot is None:
            better = True
        elif (dot >= 0) != (best_dot >= 0):
            better = dot >= 0
        else:
            better = cross * best_dot < best_cross * dot

        if better:
            best_cross, best_dot = cross, dot
            answer_a, answer_b = i, j

        previous = current

    print(answer_a, answer_b)


if __name__ == "__main__":
    main()