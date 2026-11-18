import sys
from collections import deque

def neg(v):
    return (-v[0], -v[1], -v[2])

def main():
    grid = sys.stdin.read().split()
    cells = {(r, c) for r, row in enumerate(grid)
             for c, ch in enumerate(row) if ch == '#'}

    start = next(iter(cells))
    orientations = {start: ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
    queue = deque([start])

    while queue:
        r, c = queue.popleft()
        u, v, n = orientations[(r, c)]
        neighbors = [
            ((r, c + 1), (neg(n), v, u)),
            ((r, c - 1), (n, v, neg(u))),
            ((r + 1, c), (u, neg(n), v)),
            ((r - 1, c), (u, n, neg(v))),
        ]
        for cell, orientation in neighbors:
            if cell not in cells:
                continue
            if cell in orientations:
                if orientations[cell] != orientation:
                    print("cannot fold")
                    return
            else:
                orientations[cell] = orientation
                queue.append(cell)

    normals = {orientation[2] for orientation in orientations.values()}
    print("can fold" if len(normals) == 6 else "cannot fold")

if __name__ == "__main__":
    main()