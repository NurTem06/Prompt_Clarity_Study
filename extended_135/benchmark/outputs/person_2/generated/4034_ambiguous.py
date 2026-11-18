import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    s = data[1]
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                graph[i].append(j)
                graph[j].append(i)

    colors = [-1] * n
    for start in range(n):
        if colors[start] != -1:
            continue
        colors[start] = 0
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if colors[v] == -1:
                    colors[v] = colors[u] ^ 1
                    queue.append(v)
                elif colors[v] == colors[u]:
                    print("NO")
                    return

    print("YES")
    print("".join(map(str, colors)))


if __name__ == "__main__":
    main()