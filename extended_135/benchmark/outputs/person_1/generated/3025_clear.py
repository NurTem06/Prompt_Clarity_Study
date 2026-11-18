import sys
import heapq
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    gold = [0, 0] + data[2:n]
    adj = [[] for _ in range(n)]
    masks = [0] * n

    pos = n
    for _ in range(m):
        a, b = data[pos] - 1, data[pos + 1] - 1
        pos += 2
        adj[a].append(b)
        adj[b].append(a)
        masks[a] |= 1 << b
        masks[b] |= 1 << a

    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        return dist

    ds = bfs(0)
    dt = bfs(1)
    length = ds[1]

    if length == 1:
        print(0)
        return

    bits = [1 << v for v in range(n)]

    # Villages whose removal separates home and castle cannot be robbed.
    for removed in range(2, n):
        if ds[removed] + dt[removed] != length:
            continue
        seen = bits[removed] | 1
        frontier = 1
        while frontier and not (seen & 2):
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            new = masks[v] & ~seen
            seen |= new
            frontier |= new
        if not (seen & 2):
            gold[removed] = 0

    order = sorted(range(n), key=lambda v: ds[v], reverse=True)
    children = [[] for _ in range(n)]
    suffix = [0] * n

    for v in order:
        if ds[v] + dt[v] != length:
            continue
        nxt = [
            w for w in adj[v]
            if ds[w] == ds[v] + 1 and ds[w] + dt[w] == length
        ]
        nxt.sort(key=lambda w: gold[w] + suffix[w], reverse=True)
        children[v] = nxt
        if nxt:
            suffix[v] = gold[nxt[0]] + suffix[nxt[0]]

    push = heapq.heappush
    pop = heapq.heappop
    infinity = 10**9

    def return_cost(blocked, limit):
        visited = 0
        distances = [infinity] * n
        distances[0] = 0
        heap = [(0, 0)]
        free = ~blocked

        while heap:
            cost, start = pop(heap)
            start_bit = bits[start]
            if visited & start_bit:
                continue
            if cost >= limit:
                return limit

            frontier = start_bit
            boundary = 0
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                visited |= bit
                if bit == 2:
                    return cost
                v = bit.bit_length() - 1
                neighbors = masks[v]
                boundary |= neighbors
                frontier |= neighbors & free & ~visited

            boundary &= blocked & ~visited
            while boundary:
                bit = boundary & -boundary
                boundary ^= bit
                v = bit.bit_length() - 1
                new_cost = cost + gold[v]
                if new_cost < limit and new_cost < distances[v]:
                    distances[v] = new_cost
                    push(heap, (new_cost, v))

        return limit

    best = 0

    def search(v, blocked, total):
        nonlocal best
        upper = total + suffix[v]
        if upper <= best:
            return

        limit = upper - best
        penalty = return_cost(blocked, limit)
        if penalty >= limit:
            return

        if v == 1:
            best = total - penalty
            return

        for w in children[v]:
            value = gold[w]
            search(w, blocked | (bits[w] if value else 0), total + value)
            if best >= upper - penalty:
                break

    search(0, 0, 0)
    print(best)


if __name__ == "__main__":
    main()
