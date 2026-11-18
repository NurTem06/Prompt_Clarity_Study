import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(data) - 1
        v = next(data) - 1
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        queue = [start]
        for u in queue:
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
        return queue[-1], dist, parent

    a, _, _ = bfs(0)
    b, distances, parent = bfs(a)
    diameter = distances[b]

    dist = [-1] * n
    queue = []
    u = b
    while u != -1:
        queue.append(u)
        dist[u] = 0
        u = parent[u]

    interior = queue[1]
    for u in queue:
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    c = queue[-1]
    if dist[c] == 0:
        c = interior

    print(diameter + dist[c])
    print(a + 1, b + 1, c + 1)


if __name__ == "__main__":
    main()
