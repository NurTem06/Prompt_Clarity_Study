import sys
from collections import deque


def main():
    data = sys.stdin.buffer
    h, w = map(int, data.readline().split())
    grid = [data.readline().strip() for _ in range(h)]
    commands = data.readline().strip()

    ids = [[-1] * w for _ in range(h)]
    cells = []
    start = goal = -1

    for r in range(h):
        for c in range(w):
            if grid[r][c] != 35:
                p = len(cells)
                ids[r][c] = p
                cells.append((r, c))
                if grid[r][c] == 83:
                    start = p
                elif grid[r][c] == 71:
                    goal = p

    count = len(cells)
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
    transitions = []
    neighbors = []

    for p, (r, c) in enumerate(cells):
        moves = []
        adjacent = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and ids[nr][nc] != -1:
                q = ids[nr][nc]
                moves.append(q)
                adjacent.append(q)
            else:
                moves.append(p)
        transitions.append(moves)
        neighbors.append(adjacent)

    command_ids = [{76: 0, 82: 1, 85: 2, 68: 3}[c] for c in commands]
    n = len(command_ids)
    size = (n + 1) * count
    dist = [10**9] * size
    settled = bytearray(size)
    dist[start] = 0
    queue = deque([start])

    while queue:
        state = queue.popleft()
        if settled[state]:
            continue
        settled[state] = 1

        i, p = divmod(state, count)
        cost = dist[state]
        if p == goal:
            print(cost)
            return

        offset = i * count

        if i < n:
            target = offset + count + transitions[p][command_ids[i]]
            if cost < dist[target]:
                dist[target] = cost
                queue.appendleft(target)

            target = state + count
            if cost + 1 < dist[target]:
                dist[target] = cost + 1
                queue.append(target)

        new_cost = cost + 1
        for q in neighbors[p]:
            target = offset + q
            if new_cost < dist[target]:
                dist[target] = new_cost
                queue.append(target)


if __name__ == "__main__":
    main()
