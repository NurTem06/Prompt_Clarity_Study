import sys
from collections import deque


def main():
    data = sys.stdin.buffer
    first = data.readline().split()
    if not first:
        return

    size = first[0][0] - ord('a') + 1
    n = int(first[1])
    graph = [set() for _ in range(size)]
    indegree = [0] * size
    previous = data.readline().strip()
    impossible = False

    for _ in range(n - 1):
        current = data.readline().strip()
        for a, b in zip(previous, current):
            if a != b:
                u = a - 97
                v = b - 97
                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[v] += 1
                break
        else:
            if len(previous) > len(current):
                impossible = True
        previous = current

    if impossible:
        print("IMPOSSIBLE")
        return

    ready = deque(i for i in range(size) if indegree[i] == 0)
    order = []
    ambiguous = False

    while ready:
        if len(ready) > 1:
            ambiguous = True
        u = ready.popleft()
        order.append(chr(u + 97))
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)

    if len(order) != size:
        print("IMPOSSIBLE")
    elif ambiguous:
        print("AMBIGUOUS")
    else:
        print("".join(order))


if __name__ == "__main__":
    main()