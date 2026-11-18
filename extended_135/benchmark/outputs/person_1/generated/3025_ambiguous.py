import sys
import heapq
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    gold = [0, 0] + data[2:n]
    adj = [0] * n
    pos = n
    for _ in range(m):
        a, b = data[pos] - 1, data[pos + 1] - 1
        pos += 2
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    full = (1 << n) - 1
    target = 2

    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            neighbors = adj[v]
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                u = bit.bit_length() - 1
                if dist[u] == -1:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        return dist

    ds = bfs(0)
    dt = bfs(1)
    length = ds[1]

    if length == 1:
        print(0)
        return

    on_shortest = [
        ds[v] + dt[v] == length
        for v in range(n)
    ]

    # A vertex separating home from the castle can never be robbed.
    for v in range(2, n):
        if not on_shortest[v]:
            continue
        unseen = full ^ (1 << v) ^ 1
        frontier = 1
        reachable = False
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            u = bit.bit_length() - 1
            neighbors = adj[u] & unseen
            if neighbors & target:
                reachable = True
                break
            unseen ^= neighbors
            frontier |= neighbors
        if not reachable:
            gold[v] = 0

    children = [[] for _ in range(n)]
    for v in range(n):
        if not on_shortest[v] or v == 1:
            continue
        neighbors = adj[v]
        while neighbors:
            bit = neighbors & -neighbors
            neighbors ^= bit
            u = bit.bit_length() - 1
            if on_shortest[u] and ds[u] == ds[v] + 1:
                children[v].append(u)

    tail = [0] * n
    order = sorted(range(n), key=ds.__getitem__, reverse=True)
    for v in order:
        if children[v]:
            tail[v] = gold[v] + max(tail[u] for u in children[v])
        else:
            tail[v] = gold[v]

    for neighbors in children:
        neighbors.sort(key=tail.__getitem__, reverse=True)

    if tail[0] == 0:
        print(0)
        return

    heappush = heapq.heappush
    heappop = heapq.heappop

    def minimum_loss(blocked, limit):
        zero_mask = full ^ blocked
        unseen = full ^ 1
        frontier = 1
        heap = []
        cost = 0

        while True:
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                v = bit.bit_length() - 1
                neighbors = adj[v] & unseen

                if neighbors & target:
                    return cost

                unseen ^= neighbors
                frontier |= neighbors & zero_mask
                weighted = neighbors & blocked

                while weighted:
                    next_bit = weighted & -weighted
                    weighted ^= next_bit
                    u = next_bit.bit_length() - 1
                    new_cost = cost + gold[u]
                    if new_cost < limit:
                        heappush(heap, (new_cost, u))

            if not heap:
                return limit

            cost, v = heappop(heap)
            frontier = 1 << v

    best = 0

    def search(v, total, blocked):
        nonlocal best

        if total + tail[v] - gold[v] <= best:
            return

        if v == 1:
            loss = minimum_loss(blocked, total - best)
            candidate = total - loss
            if candidate > best:
                best = candidate
            return

        for u in children[v]:
            if total + tail[u] <= best:
                break
            value = gold[u]
            search(
                u,
                total + value,
                blocked | (1 << u) if value else blocked
            )

    search(0, 0, 0)
    print(best)


if __name__ == "__main__":
    main()
