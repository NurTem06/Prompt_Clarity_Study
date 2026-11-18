import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    segments = []
    for i in range(n):
        k = 1 + 4 * i
        ax, ay, bx, by = data[k:k + 4]
        if (ax, ay) > (bx, by):
            ax, ay, bx, by = bx, by, ax, ay
        segments.append((
            ax, ay, bx, by,
            bx - ax, by - ay,
            min(ay, by), max(ay, by)
        ))

    segments.sort()
    points = set()
    offset = 1 << 63

    for i in range(n):
        ax, ay, bx, by, rx, ry, ymin, ymax = segments[i]

        for j in range(i + 1, n):
            cx, cy, dx, dy, sx, sy, vmin, vmax = segments[j]

            if cx > bx:
                break
            if ymax < vmin or vmax < ymin:
                continue

            qx = cx - ax
            qy = cy - ay
            denominator = rx * sy - ry * sx

            if denominator == 0:
                if qx * ry != qy * rx:
                    continue

                if (ax, ay) >= (cx, cy):
                    low_x, low_y = ax, ay
                else:
                    low_x, low_y = cx, cy

                if (bx, by) <= (dx, dy):
                    high_x, high_y = bx, by
                else:
                    high_x, high_y = dx, dy

                if (low_x, low_y) < (high_x, high_y):
                    print(-1)
                    return
                if low_x == high_x and low_y == high_y:
                    key = (
                        ((low_x + offset) << 107)
                        | ((low_y + offset) << 43)
                        | 1
                    )
                    points.add(key)
                continue

            t = qx * sy - qy * sx
            u = qx * ry - qy * rx

            if denominator < 0:
                denominator = -denominator
                t = -t
                u = -u

            if not (0 <= t <= denominator and 0 <= u <= denominator):
                continue

            xnum = ax * denominator + rx * t
            ynum = ay * denominator + ry * t
            common = gcd(gcd(xnum, ynum), denominator)

            xnum //= common
            ynum //= common
            denominator //= common

            key = (
                ((xnum + offset) << 107)
                | ((ynum + offset) << 43)
                | denominator
            )
            points.add(key)

    print(len(points))


if __name__ == "__main__":
    main()