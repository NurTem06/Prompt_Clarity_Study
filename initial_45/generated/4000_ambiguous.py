import sys
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    graph = [[] for _ in range(n + 1)]
    for i in range(1, len(data), 2):
        u, v = data[i], data[i + 1]
        graph[u].append(v)
        graph[v].append(u)
    del data

    def bfs(start):
        parent = [-1] * (n + 1)
        parent[start] = 0
        distance = [0] * (n + 1)
        queue = deque([start])
        last = start
        while queue:
            u = queue.popleft()
            last = u
            for v in graph[u]:
                if parent[v] == -1:
                    parent[v] = u
                    distance[v] = distance[u] + 1
                    queue.append(v)
        return last, parent, distance[last]

    a, _, _ = bfs(1)
    b, parent, diameter = bfs(a)

    distance = [-1] * (n + 1)
    queue = deque()
    u = b
    while u:
        distance[u] = 0
        queue.append(u)
        u = parent[u]

    c = parent[b]
    extra = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                queue.append(v)
                if distance[v] > extra:
                    extra = distance[v]
                    c = v

    print(diameter + extra)
    print(a, b, c)


if __name__ == "__main__":
    main()
