import sys
import heapq


def main():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    costs = [0] * (n * m)
    start = goal = -1
    terrain = {ord('.'): 1, ord('F'): 2, ord('M'): 3,
               ord('S'): 1, ord('G'): 1}

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            pos = r * m + c
            costs[pos] = terrain.get(ch, 0)
            if ch == ord('S'):
                start = pos
            elif ch == ord('G'):
                goal = pos

    inf = (10**9, 0)
    best = [inf] * (n * m)
    best[start] = (1, 0)
    heap = [(1, 0, start)]

    while heap:
        days, used, pos = heapq.heappop(heap)
        if best[pos] != (days, used):
            continue
        if pos == goal:
            print(days)
            return

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

        for nxt in neighbors:
            cost = costs[nxt]
            if cost == 0 or cost > k:
                continue
            if used + cost <= k:
                candidate = (days, used + cost)
            else:
                candidate = (days + 1, cost)
            if candidate < best[nxt]:
                best[nxt] = candidate
                heapq.heappush(heap, (candidate[0], candidate[1], nxt))

    print(-1)


if __name__ == "__main__":
    main()