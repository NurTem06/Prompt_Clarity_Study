import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    n, k = map(int, data[:2])
    s = data[2]

    if k == 1:
        print(0)
        return

    seen = {s}
    queue = deque([s])
    total_cost = 0

    while queue:
        current = queue.popleft()
        cost = n - len(current) + 1

        for i in range(len(current)):
            if i > 0 and current[i] == current[i - 1]:
                continue

            candidate = current[:i] + current[i + 1:]
            if candidate in seen:
                continue

            seen.add(candidate)
            total_cost += cost

            if len(seen) == k:
                print(total_cost)
                return

            queue.append(candidate)

    print(-1)


if __name__ == "__main__":
    main()
