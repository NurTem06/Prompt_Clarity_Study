import sys
from math import gcd

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, r = data[:3]
    pos = 3
    points = []
    for _ in range(n):
        points.append((data[pos], data[pos + 1]))
        pos += 2

    lines = []
    regions = 1
    r2 = r * r

    for _ in range(m):
        a, b, c = data[pos:pos + 3]
        pos += 3
        intersections = set()

        for aa, bb, cc in lines:
            det = a * bb - aa * b
            if det == 0:
                continue

            xnum = b * cc - bb * c
            ynum = c * aa - cc * a

            if xnum * xnum + ynum * ynum >= r2 * det * det:
                continue

            if det < 0:
                xnum, ynum, det = -xnum, -ynum, -det

            g = gcd(gcd(abs(xnum), abs(ynum)), det)
            intersections.add((xnum // g, ynum // g, det // g))

        regions += len(intersections) + 1
        lines.append((a, b, c))

    if regions != n:
        print("no")
        return

    occupied = set()
    for x, y in points:
        mask = 0
        for i, (a, b, c) in enumerate(lines):
            if a * x + b * y + c > 0:
                mask |= 1 << i
        if mask in occupied:
            print("no")
            return
        occupied.add(mask)

    print("yes")

if __name__ == "__main__":
    main()