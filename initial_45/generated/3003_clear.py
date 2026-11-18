import sys


def main():
    stream = sys.stdin.buffer
    n = int(stream.readline())
    adjacency = [0] * n

    for u in range(n):
        for token in stream.readline().split():
            v = int(token)
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u

    size = 1 << n
    independent = [False] * size
    independent[0] = True

    for mask in range(1, size):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        rest = mask ^ bit
        independent[mask] = independent[rest] and not (adjacency[vertex] & rest)

    dp = [0] * size
    for mask in range(1, size):
        if independent[mask]:
            dp[mask] = 1
            continue

        anchor = mask & -mask
        rest = mask ^ anchor
        best = n
        sub = rest

        while True:
            group = sub | anchor
            if independent[group]:
                best = min(best, 1 + dp[mask ^ group])
                if best == 2:
                    break
            if sub == 0:
                break
            sub = (sub - 1) & rest

        dp[mask] = best

    print(dp[-1])


if __name__ == "__main__":
    main()
