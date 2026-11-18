import sys
import heapq


def main():
    read = sys.stdin.buffer.readline
    n, m, s, t = map(int, read().split())

    if s == t:
        print(0)
        return

    reverse = [[] for _ in range(n)]
    remaining = [0] * n

    for _ in range(m):
        a, b, w = map(int, read().split())
        reverse[b].append((a, w))
        remaining[a] += 1

    # Even states: maximizing player's turn.
    # Odd states: minimizing player's turn.
    distance = [-1] * (2 * n)
    maximum = [0] * n
    distance[2 * t] = distance[2 * t + 1] = 0
    heap = [(0, 2 * t), (0, 2 * t + 1)]
    push = heapq.heappush
    pop = heapq.heappop
    start = 2 * s

    while heap:
        value, state = pop(heap)
        if distance[state] != value:
            continue

        if state == start:
            print(value)
            return

        node = state >> 1

        if state & 1:
            # A maximizing predecessor needs all successors to be finite.
            for predecessor, weight in reverse[node]:
                if predecessor == t:
                    continue
                candidate = value + weight
                if candidate > maximum[predecessor]:
                    maximum[predecessor] = candidate
                remaining[predecessor] -= 1
                if remaining[predecessor] == 0:
                    previous_state = predecessor << 1
                    distance[previous_state] = maximum[predecessor]
                    push(heap, (maximum[predecessor], previous_state))
        else:
            # A minimizing predecessor can choose any finite successor.
            for predecessor, weight in reverse[node]:
                if predecessor == t:
                    continue
                previous_state = (predecessor << 1) | 1
                candidate = value + weight
                old = distance[previous_state]
                if old == -1 or candidate < old:
                    distance[previous_state] = candidate
                    push(heap, (candidate, previous_state))

    print("infinity")


if __name__ == "__main__":
    main()
