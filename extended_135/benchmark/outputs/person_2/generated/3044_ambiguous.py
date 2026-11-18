import sys
from collections import deque


def main():
    data = sys.stdin.buffer
    h, w = map(int, data.readline().split())
    grid = [data.readline().strip() for _ in range(h)]
    commands = data.readline().strip()

    size = h * w
    transitions = [None] * size
    start = goal = -1
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

    for r in range(h):
        for c in range(w):
            if grid[r][c] == 35:
                continue
            pos = r * w + c
            if grid[r][c] == 83:
                start = pos
            elif grid[r][c] == 71:
                goal = pos

            moves = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 35:
                    moves.append(nr * w + nc)
                else:
                    moves.append(pos)
            transitions[pos] = moves

    mapping = {76: 0, 82: 1, 85: 2, 68: 3}
    program = [mapping[ch] for ch in commands]
    n = len(program)

    total = (n + 1) * size
    dist = [10**9] * total
    done = bytearray(total)
    dist[start] = 0
    queue = deque([start])

    while queue:
        state = queue.popleft()
        if done[state]:
            continue
        done[state] = 1

        index, pos = divmod(state, size)
        cost = dist[state]

        if pos == goal:
            print(cost)
            return

        base = state - pos
        moves = transitions[pos]

        if index < n:
            next_base = base + size

            nxt = next_base + moves[program[index]]
            if cost < dist[nxt]:
                dist[nxt] = cost
                queue.appendleft(nxt)

            nxt = next_base + pos
            if cost + 1 < dist[nxt]:
                dist[nxt] = cost + 1
                queue.append(nxt)

        for next_pos in moves:
            if next_pos == pos:
                continue
            nxt = base + next_pos
            if cost + 1 < dist[nxt]:
                dist[nxt] = cost + 1
                queue.append(nxt)


if __name__ == "__main__":
    main()
