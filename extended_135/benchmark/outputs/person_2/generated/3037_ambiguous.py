import sys
from array import array


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def main():
    read = sys.stdin.buffer.readline
    h, w, n = map(int, read().split())
    size = h * w

    board = bytearray()
    for _ in range(h):
        board.extend(read().strip())

    remaining = board.count(35)
    commands = array('I')
    codes = {b'up': 0, b'down': 1, b'left': 2, b'right': 3}

    x = 0
    y = h - 1
    time = 1

    for _ in range(n):
        direction, value = read().split()
        distance = int(value)
        code = codes[direction]
        commands.append((distance << 2) | code)
        time += distance
        if code == 0:
            y -= distance
        elif code == 1:
            y += distance
        elif code == 2:
            x -= distance
        else:
            x += distance

    lower = 0
    upper = time
    rows = array('I', range(size + 1))
    cols = array('I', range(size + 1))
    get = find

    for encoded in reversed(commands):
        code = encoded & 3
        distance = encoded >> 2

        if code >= 2:
            base = y * w
            end = base + x

            if code == 3:
                first = end - distance + 1
                last = end
                offset = time - end
                sign = 1
            else:
                first = end
                last = end + distance - 1
                offset = time + end
                sign = -1

            pos = get(rows, first)
            while pos <= last:
                visit = offset + sign * pos
                if board[pos] == 35:
                    remaining -= 1
                    if visit > lower:
                        lower = visit
                elif visit - 1 < upper:
                    upper = visit - 1

                if lower > upper:
                    sys.stdout.write("-1 -1\n")
                    return

                other = (pos - base) * h + y
                rows[pos] = get(rows, pos + 1)
                cols[other] = get(cols, other + 1)
                pos = rows[pos]

            if code == 3:
                x -= distance
            else:
                x += distance

        else:
            base = x * h
            end = base + y

            if code == 1:
                first = end - distance + 1
                last = end
                offset = time - end
                sign = 1
            else:
                first = end
                last = end + distance - 1
                offset = time + end
                sign = -1

            pos = get(cols, first)
            while pos <= last:
                other = (pos - base) * w + x
                visit = offset + sign * pos

                if board[other] == 35:
                    remaining -= 1
                    if visit > lower:
                        lower = visit
                elif visit - 1 < upper:
                    upper = visit - 1

                if lower > upper:
                    sys.stdout.write("-1 -1\n")
                    return

                cols[pos] = get(cols, pos + 1)
                rows[other] = get(rows, other + 1)
                pos = cols[pos]

            if code == 1:
                y -= distance
            else:
                y += distance

        time -= distance

    start = (h - 1) * w
    if get(rows, start) == start:
        if board[start] == 35:
            remaining -= 1
            lower = max(lower, 1)
        else:
            upper = 0

    if remaining or lower > upper:
        sys.stdout.write("-1 -1\n")
    else:
        sys.stdout.write(f"{lower} {upper}\n")


if __name__ == "__main__":
    main()
