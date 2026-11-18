import sys
from array import array


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def main():
    inp = sys.stdin.buffer
    h, w, n = map(int, inp.readline().split())
    board = bytearray()
    for _ in range(h):
        board.extend(inp.readline().strip())

    directions = bytearray()
    distances = array('I')
    r, c = h - 1, 0
    total = 1

    for _ in range(n):
        direction, value = inp.readline().split()
        d = direction[0]
        length = int(value)
        directions.append(d)
        distances.append(length)
        total += length
        if d == 117:
            r -= length
        elif d == 100:
            r += length
        elif d == 108:
            c -= length
        else:
            c += length

    size = h * w
    rows = array('I', range(size + 1))
    cols = array('I', range(size + 1))
    remaining = board.count(35)
    lower, upper = 0, total
    time = total
    visited = 0

    for k in range(n - 1, -1, -1):
        d = directions[k]
        length = distances[k]

        if d == 117:
            horizontal = False
            base = c * h
            lo = base + r
            hi = lo + length - 1
            first_time = time
            slope = -1
            fixed = c
            r += length
        elif d == 100:
            horizontal = False
            base = c * h
            hi = base + r
            lo = hi - length + 1
            first_time = time - length + 1
            slope = 1
            fixed = c
            r -= length
        elif d == 108:
            horizontal = True
            base = r * w
            lo = base + c
            hi = lo + length - 1
            first_time = time
            slope = -1
            fixed = r
            c += length
        else:
            horizontal = True
            base = r * w
            hi = base + c
            lo = hi - length + 1
            first_time = time - length + 1
            slope = 1
            fixed = r
            c -= length

        if horizontal:
            parent, other = rows, cols
            stride = h
        else:
            parent, other = cols, rows
            stride = w

        p = find(parent, lo)
        while p <= hi:
            cross = (p - base) * stride + fixed
            cell = p if horizontal else cross
            last_time = first_time + slope * (p - lo)

            if board[cell] == 35:
                remaining -= 1
                if last_time > lower:
                    lower = last_time
            elif last_time - 1 < upper:
                upper = last_time - 1

            if lower > upper:
                print("-1 -1")
                return

            nxt = find(parent, p + 1)
            parent[p] = nxt
            other[cross] = find(other, cross + 1)
            p = nxt
            visited += 1

        time -= length
        if visited == size:
            break

    start = (h - 1) * w
    if find(rows, start) == start:
        if board[start] == 35:
            remaining -= 1
            if lower < 1:
                lower = 1
        else:
            upper = 0

    if remaining or lower > upper:
        print("-1 -1")
    else:
        print(lower, upper)


if __name__ == "__main__":
    main()
