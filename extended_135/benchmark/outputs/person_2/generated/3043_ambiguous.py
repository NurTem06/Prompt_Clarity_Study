import sys
import heapq


def main():
    data = sys.stdin.buffer
    n, m, k = map(int, data.readline().split())
    grid = [data.readline().strip() for _ in range(n)]
    size = n * m
    costs = [0] * size
    start = goal = -1

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            pos = r * m + c
            if ch == ord('#'):
                continue
            if ch == ord('F'):
                costs[pos] = 2
            elif ch == ord('M'):
                costs[pos] = 3
            else:
                costs[pos] = 1
            if ch == ord('S'):
                start = pos
            elif ch == ord('G'):
                goal = pos

    adjacency = [[] for _ in range(size)]
    for pos in range(size):
        if not costs[pos] or costs[pos] > k:
            continue
        r, c = divmod(pos, m)
        neighbors = []
        if r:
            neighbors.append(pos - m)
        if r + 1 < n:
            neighbors.append(pos + m)
        if c:
            neighbors.append(pos - 1)
        if c + 1 < m:
            neighbors.append(pos + 1)
        adjacency[pos] = [
            (v, costs[v]) for v in neighbors if 0 < costs[v] <= k
        ]

    stride = k + 1
    inf = 10**18
    dist = [inf] * size
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        current, pos = heapq.heappop(heap)
        if current != dist[pos]:
            continue
        if pos == goal:
            print(current // stride + 1)
            return

        day, used = divmod(current, stride)
        base = day * stride
        for nxt, cost in adjacency[pos]:
            if used + cost <= k:
                candidate = current + cost
            else:
                candidate = base + stride + cost
            if candidate < dist[nxt]:
                dist[nxt] = candidate
                heapq.heappush(heap, (candidate, nxt))

    print(-1)


if __name__ == "__main__":
    main()
