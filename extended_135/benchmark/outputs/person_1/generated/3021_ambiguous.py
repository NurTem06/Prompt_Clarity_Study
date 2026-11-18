import sys
from collections import deque


def main():
    data = sys.stdin.buffer
    first = data.readline().split()
    if not first:
        return

    k = first[0][0] - ord('a') + 1
    n = int(first[1])
    graph = [set() for _ in range(k)]
    indegree = [0] * k

    previous = data.readline().strip()
    for _ in range(n - 1):
        current = data.readline().strip()
        limit = min(len(previous), len(current))

        for i in range(limit):
            if previous[i] != current[i]:
                u = previous[i] - 97
                v = current[i] - 97
                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[v] += 1
                break
        else:
            if len(previous) > len(current):
                print("IMPOSSIBLE")
                return

        previous = current

    available = deque(i for i in range(k) if indegree[i] == 0)
    order = []
    ambiguous = False

    while available:
        if len(available) > 1:
            ambiguous = True

        u = available.popleft()
        order.append(chr(u + 97))

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                available.append(v)

    if len(order) != k:
        print("IMPOSSIBLE")
    elif ambiguous:
        print("AMBIGUOUS")
    else:
        print("".join(order))


if __name__ == "__main__":
    main()