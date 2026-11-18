import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    segments = []
    for k in range(1, 4 * n + 1, 4):
        x0, y0, x1, y1 = data[k:k + 4]
        if x0 > x1 or (x0 == x1 and y0 > y1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        segments.append((
            x0, y0, x1, y1,
            x1 - x0, y1 - y0,
            min(y0, y1), max(y0, y1)
        ))
    del data

    points = set()
    offset = 1 << 63

    for i in range(n):
        ax, ay, bx, by, rx, ry, low_y, high_y = segments[i]

        for j in range(i):
            cx, cy, dx, dy, sx, sy, other_low_y, other_high_y = segments[j]

            if (bx < cx or dx < ax or
                    high_y < other_low_y or other_high_y < low_y):
                continue

            qx = cx - ax
            qy = cy - ay
            denominator = rx * sy - ry * sx

            if denominator == 0:
                if qx * ry - qy * rx != 0:
                    continue

                if rx:
                    left = max(ax, cx)
                    right = min(bx, dx)
                else:
                    left = max(ay, cy)
                    right = min(by, dy)

                if left < right:
                    print(-1)
                    return
                if left > right:
                    continue

                if ax > cx or (ax == cx and ay >= cy):
                    px, py = ax, ay
                else:
                    px, py = cx, cy

                points.add(
                    ((px + offset) << 107) |
                    ((py + offset) << 43) |
                    1
                )
                continue

            t = qx * sy - qy * sx
            u = qx * ry - qy * rx

            if denominator < 0:
                denominator = -denominator
                t = -t
                u = -u

            if t < 0 or t > denominator or u < 0 or u > denominator:
                continue

            px = ax * denominator + rx * t
            py = ay * denominator + ry * t
            common = gcd(gcd(px, py), denominator)

            if common != 1:
                px //= common
                py //= common
                denominator //= common

            points.add(
                ((px + offset) << 107) |
                ((py + offset) << 43) |
                denominator
            )

    print(len(points))


if __name__ == "__main__":
    main()
