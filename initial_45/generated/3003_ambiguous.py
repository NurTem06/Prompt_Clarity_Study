import sys


def main():
    data = sys.stdin.buffer
    line = data.readline()
    if not line:
        return
    n = int(line)
    adjacency = [0] * n

    for u in range(n):
        for v in map(int, data.readline().split()):
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u

    size = 1 << n
    independent = bytearray(size)
    independent[0] = 1

    for mask in range(1, size):
        bit = mask & -mask
        rest = mask ^ bit
        vertex = bit.bit_length() - 1
        independent[mask] = (
            independent[rest] and not (adjacency[vertex] & rest)
        )

    dp = [0] * size
    for mask in range(1, size):
        if independent[mask]:
            dp[mask] = 1
            continue

        bit = mask & -mask
        rest = mask ^ bit
        best = dp[rest] + 1
        subset = rest

        while subset:
            color_class = subset | bit
            if independent[color_class]:
                candidate = dp[mask ^ color_class] + 1
                if candidate < best:
                    best = candidate
                    if best == 2:
                        break
            subset = (subset - 1) & rest

        dp[mask] = best

    print(dp[-1])


if __name__ == "__main__":
    main()