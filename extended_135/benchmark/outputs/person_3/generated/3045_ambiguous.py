import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    beacons = []
    low_u = low_v = -10**30
    high_u = high_v = 10**30

    for i in range(n):
        x, y, d = data[1 + 3 * i:4 + 3 * i]
        u, v = x + y, x - y
        beacons.append((u, v, d))
        low_u = max(low_u, u - d)
        high_u = min(high_u, u + d)
        low_v = max(low_v, v - d)
        high_v = min(high_v, v + d)

    if low_u > high_u or low_v > high_v:
        print("impossible")
        return

    solutions = set()
    edges = [
        (0, low_u, low_v, high_v),
        (0, high_u, low_v, high_v),
        (1, low_v, low_u, high_u),
        (1, high_v, low_u, high_u),
    ]

    for axis, fixed, lower, upper in edges:
        candidates = None

        for u, v, d in beacons:
            center_fixed, center_variable = (u, v) if axis == 0 else (v, u)
            if abs(fixed - center_fixed) != d:
                candidates = (center_variable - d, center_variable + d)
                break

        if candidates is None:
            first = lower + ((fixed - lower) & 1)
            candidates = (first, first + 2)

        for variable in candidates:
            if not lower <= variable <= upper or (fixed - variable) & 1:
                continue

            u, v = (fixed, variable) if axis == 0 else (variable, fixed)
            if all(max(abs(u - bu), abs(v - bv)) == d
                   for bu, bv, d in beacons):
                solutions.add((u, v))
                if len(solutions) > 1:
                    print("uncertain")
                    return

    if not solutions:
        print("impossible")
    else:
        u, v = next(iter(solutions))
        print((u + v) // 2, (u - v) // 2)


if __name__ == "__main__":
    main()
