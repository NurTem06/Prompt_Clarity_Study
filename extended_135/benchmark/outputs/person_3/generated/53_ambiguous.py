import sys
import heapq
from collections import Counter

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    beauty = list(map(int, data[2:2 + n]))

    counts = Counter(s)
    letters = list(counts)
    k = len(letters)
    pairs = n // 2

    source = 0
    pair_start = k + 1
    sink = pair_start + pairs
    size = sink + 1
    graph = [[] for _ in range(size)]

    def add_edge(u, v, capacity, cost):
        graph[u].append([v, len(graph[v]), capacity, cost])
        graph[v].append([u, len(graph[u]) - 1, 0, -cost])

    for j, letter in enumerate(letters, 1):
        add_edge(source, j, counts[letter], 0)
        for i in range(pairs):
            opposite = n - 1 - i
            reward = 0
            if s[i] == letter:
                reward = beauty[i]
            if s[opposite] == letter:
                reward = max(reward, beauty[opposite])
            add_edge(j, pair_start + i, 1, 100 - reward)

    for i in range(pairs):
        add_edge(pair_start + i, sink, 2, 0)

    potential = [0] * size
    total_cost = 0
    flow = 0
    inf = 10**18

    while flow < n:
        dist = [inf] * size
        previous_vertex = [-1] * size
        previous_edge = [-1] * size
        dist[source] = 0
        queue = [(0, source)]

        while queue:
            distance, u = heapq.heappop(queue)
            if distance != dist[u]:
                continue
            for index, edge in enumerate(graph[u]):
                v, _, capacity, cost = edge
                if capacity:
                    new_distance = distance + cost + potential[u] - potential[v]
                    if new_distance < dist[v]:
                        dist[v] = new_distance
                        previous_vertex[v] = u
                        previous_edge[v] = index
                        heapq.heappush(queue, (new_distance, v))

        for v in range(size):
            if dist[v] < inf:
                potential[v] += dist[v]

        amount = n - flow
        v = sink
        while v != source:
            u = previous_vertex[v]
            edge = graph[u][previous_edge[v]]
            amount = min(amount, edge[2])
            v = u

        v = sink
        while v != source:
            u = previous_vertex[v]
            edge = graph[u][previous_edge[v]]
            total_cost += amount * edge[3]
            edge[2] -= amount
            graph[v][edge[1]][2] += amount
            v = u

        flow += amount

    print(100 * n - total_cost)

if __name__ == "__main__":
    main()