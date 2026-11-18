import sys
from math import gcd


def main():
    data = sys.stdin.buffer
    n, m = map(int, data.readline().split())
    width = 2 * m
    rows = []
    points = []

    for y in range(n):
        row = data.readline().strip()
        left = row.find(b'#')
        if left == -1:
            rows.append(0)
            continue
        right = row.rfind(b'#')
        points.append((left, y))
        if right != left:
            points.append((right, y))
        rows.append(int(row.replace(b'.', b'0').replace(b'#', b'1')[::-1], 2))

    board = 0
    for row in reversed(rows):
        board = (board << width) | row

    total = board.bit_count()
    if total == 1:
        print(1)
        return

    points.sort()

    def cross(a, b, c):
        return ((b[0] - a[0]) * (c[1] - a[1])
                - (b[1] - a[1]) * (c[0] - a[0]))

    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    hull = lower[:-1] + upper[:-1]
    shifts = set()

    for i, (x, y) in enumerate(hull):
        nx, ny = hull[(i + 1) % len(hull)]
        dx, dy = nx - x, ny - y
        if dy < 0 or (dy == 0 and dx < 0):
            dx, dy = -dx, -dy
        g = gcd(abs(dx), abs(dy))
        if g:
            step = (dy // g) * width + dx // g
            shifts.update(range(step, step * (g + 1), step))

    answer = total
    lower_bound = (total + 1) // 2

    for shift in sorted(shifts):
        if (board & ((board << shift) | (board >> shift))) != board:
            continue

        parity = board
        mask = board & (board << shift)
        step = shift

        while mask:
            parity ^= (parity << step) & mask
            mask &= mask << step
            step <<= 1

        candidate = parity.bit_count()
        if candidate < answer:
            answer = candidate
            if answer == lower_bound:
                break

    print(answer)


if __name__ == "__main__":
    main()
