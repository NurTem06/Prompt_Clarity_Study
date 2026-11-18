import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n, m, r = next(it), next(it), next(it)
    candles = [(next(it), next(it)) for _ in range(n)]
    lines = [(next(it), next(it), next(it)) for _ in range(m)]

    signatures = set()
    for x, y in candles:
        mask = 0
        for i, (a, b, c) in enumerate(lines):
            if a * x + b * y + c > 0:
                mask |= 1 << i
        signatures.add(mask)

    if len(signatures) != n:
        print("no")
        return

    pieces = 1
    radius_squared = r * r

    for i, (a, b, c) in enumerate(lines):
        intersections = set()
        for aa, bb, cc in lines[:i]:
            det = a * bb - aa * b
            if det == 0:
                continue

            nx = b * cc - bb * c
            ny = c * aa - cc * a

            if nx * nx + ny * ny >= radius_squared * det * det:
                continue

            if det < 0:
                nx, ny, det = -nx, -ny, -det
            divisor = gcd(gcd(abs(nx), abs(ny)), det)
            intersections.add((nx // divisor, ny // divisor, det // divisor))

        pieces += len(intersections) + 1
        if pieces > n:
            print("no")
            return

    print("yes" if pieces == n else "no")


if __name__ == "__main__":
    main()