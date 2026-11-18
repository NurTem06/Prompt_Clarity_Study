import sys
import heapq


def main():
    data = map(int, sys.stdin.buffer.read().split())
    try:
        n = next(data)
    except StopIteration:
        return
    m = next(data)
    s = next(data)
    t = next(data)

    if s == t:
        print(0)
        return

    reverse = [[] for _ in range(n)]
    remaining = [0] * n

    for _ in range(m):
        a = next(data)
        b = next(data)
        w = next(data)
        reverse[b].append((a, w))
        remaining[a] += 1

    inf = 10**30
    distance = [inf] * (2 * n)
    maximum = [0] * n
    settled = bytearray(2 * n)

    # States [0, n) are maximizing turns; [n, 2*n) are minimizing.
    distance[t] = distance[t + n] = 0
    heap = [(0, t), (0, t + n)]
    push = heapq.heappush
    pop = heapq.heappop

    while heap:
        d, state = pop(heap)
        if settled[state] or distance[state] != d:
            continue
        settled[state] = 1

        if state == s:
            print(d)
            return

        if state < n:
            # A minimizing predecessor may choose this successor.
            for predecessor, weight in reverse[state]:
                parent = predecessor + n
                candidate = d + weight
                if candidate < distance[parent]:
                    distance[parent] = candidate
                    push(heap, (candidate, parent))
        else:
            # A maximizing predecessor needs every successor to be finite.
            vertex = state - n
            for predecessor, weight in reverse[vertex]:
                if settled[predecessor]:
                    continue
                candidate = d + weight
                if candidate > maximum[predecessor]:
                    maximum[predecessor] = candidate
                remaining[predecessor] -= 1
                if remaining[predecessor] == 0:
                    distance[predecessor] = maximum[predecessor]
                    push(heap, (maximum[predecessor], predecessor))

    print("infinity")


if __name__ == "__main__":
    main()
