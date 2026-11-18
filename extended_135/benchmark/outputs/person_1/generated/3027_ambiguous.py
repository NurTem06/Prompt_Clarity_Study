import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n, m = map(int, data[:2])
    rows = data[2:2 + n]

    occupied_rows = [i for i, row in enumerate(rows) if b'#' in row]
    top, bottom = occupied_rows[0], occupied_rows[-1]
    left = min(rows[i].find(b'#') for i in occupied_rows)
    right = max(rows[i].rfind(b'#') for i in occupied_rows)

    rows = [row[left:right + 1] for row in rows[top:bottom + 1]]
    n = len(rows)
    m = right - left + 1
    width = 2 * m
    length = (n - 1) * width + m

    translation = bytes.maketrans(b'.#', b'01')
    shape = 0
    reflected = 0
    points = []
    total = 0

    for r, row in enumerate(rows):
        binary = row.translate(translation)
        shape |= int(binary[::-1], 2) << (r * width)
        reflected |= int(binary, 2) << ((n - 1 - r) * width)
        total += row.count(b'#')
        first = row.find(b'#')
        if first >= 0:
            last = row.rfind(b'#')
            points.append((r, first))
            if last != first:
                points.append((r, last))

    lower_bound = (total + 1) // 2
    if total == 1:
        print(1)
        return

    points.sort()

    def cross(a, b, c):
        return ((b[0] - a[0]) * (c[1] - a[1])
                - (b[1] - a[1]) * (c[0] - a[0]))

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]

    anchor = (shape & -shape).bit_length() - 1
    candidates = (shape >> anchor) & ~1

    for r, c in hull:
        p = r * width + c
        candidates &= (shape >> p) | (reflected >> (length - 1 - p))
        if not candidates:
            print(total)
            return

    best = total

    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        shift = bit.bit_length() - 1

        isolated = shape & ~((shape << shift) | (shape >> shift))
        if isolated:
            p = (isolated & -isolated).bit_length() - 1
            candidates &= (shape >> p) | (reflected >> (length - 1 - p))
            continue

        parity = shape
        run = shape & (shape << shift)
        step = shift
        while run:
            parity ^= (parity << step) & run
            run &= run << step
            step <<= 1

        count = parity.bit_count()
        if count < best:
            best = count
            if best == lower_bound:
                break

    print(best)


if __name__ == "__main__":
    main()
