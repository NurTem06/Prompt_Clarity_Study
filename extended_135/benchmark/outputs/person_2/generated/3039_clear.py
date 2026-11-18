import sys
from collections import deque


def main():
    grid = sys.stdin.read().split()
    cells = {(r, c) for r in range(6) for c in range(6) if grid[r][c] == '#'}

    def neg(v):
        return tuple(-x for x in v)

    start = next(iter(cells))
    orientations = {start: ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
    queue = deque([start])

    while queue:
        r, c = queue.popleft()
        right, down, normal = orientations[(r, c)]

        neighbors = [
            ((r, c + 1), (neg(normal), down, right)),
            ((r, c - 1), (normal, down, neg(right))),
            ((r + 1, c), (right, neg(normal), down)),
            ((r - 1, c), (right, normal, neg(down))),
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