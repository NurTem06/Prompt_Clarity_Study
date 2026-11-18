import sys


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    program = data.readline().strip()
    grid = b"".join(data.readline().strip() for _ in range(n))

    pos = grid.index(b"R")
    offsets = {60: -1, 62: 1, 94: -n, 118: n}
    commands = [(offsets[c], c) for c in program]

    seen = [-1] * (n * n)
    trail = bytearray()

    while seen[pos] == -1:
        seen[pos] = len(trail)
        for offset, command in commands:
            nxt = pos + offset
            if grid[nxt] != 35:
                pos = nxt
                trail.append(command)

    start = seen[pos]
    if start == len(trail):
        print(1)
        return

    cycle = trail[start:]
    del trail

    length = len(cycle)
    remaining = length
    factors = []

    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)

    for factor in factors:
        while length % factor == 0:
            candidate = length // factor
            if cycle[:length - candidate] != cycle[candidate:length]:
                break
            length = candidate

    print(length)


if __name__ == "__main__":
    main()
