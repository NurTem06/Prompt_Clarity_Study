import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    beacons = []
    ulo = vlo = -10**18
    uhi = vhi = 10**18

    for i in range(n):
        x, y, d = data[1 + 3 * i:4 + 3 * i]
        u, v = x + y, x - y
        beacons.append((u, v, d))
        ulo = max(ulo, u - d)
        uhi = min(uhi, u + d)
        vlo = max(vlo, v - d)
        vhi = min(vhi, v + d)

    if ulo > uhi or vlo > vhi:
        print("impossible")
        return

    u0, v0, d0 = beacons[0]
    solutions = set()

    for axis, fixed in (
        (0, u0 - d0),
        (0, u0 + d0),
        (1, v0 - d0),
        (1, v0 + d0),
    ):
        if axis == 0:
            if not ulo <= fixed <= uhi:
                continue
            low, high = vlo, vhi
        else:
            if not vlo <= fixed <= vhi:
                continue
            low, high = ulo, uhi

        candidates = None
        for u, v, d in beacons:
            center = u if axis == 0 else v
            if abs(fixed - center) != d:
                other = v if axis == 0 else u
                candidates = (other - d, other + d)
                break

        if candidates is None:
            first = low + ((fixed - low) & 1)
            candidates = (first, first + 2)

        for variable in candidates:
            if not low <= variable <= high:
                continue
            if (fixed - variable) & 1:
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
