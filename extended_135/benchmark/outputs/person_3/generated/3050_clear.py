import sys


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    program = read().strip()
    grid = b''.join(read().strip() for _ in range(n))

    offsets = {60: -1, 62: 1, 94: -n, 118: n}
    instructions = [(offsets[c], c) for c in program]

    pos = grid.index(82)
    seen = [-1] * (n * n)
    trail = bytearray()
    append = trail.append

    while seen[pos] == -1:
        seen[pos] = len(trail)
        for offset, direction in instructions:
            nxt = pos + offset
            if grid[nxt] != 35:
                pos = nxt
                append(direction)

    del trail[:seen[pos]]

    if not trail:
        print(1)
    else:
        print((trail + trail).find(trail, 1))


if __name__ == "__main__":
    main()
