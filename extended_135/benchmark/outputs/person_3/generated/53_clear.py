import sys
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    beauty = list(map(int, data[2:2 + n]))

    counts = [0] * 26
    for c in s:
        counts[c - 97] += 1

    letters = [c for c in range(26) if counts[c]]
    k = len(letters)
    half = n // 2
    source = 0
    pair_start = k + 1
    sink = pair_start + half
    size = sink + 1
    graph = [[] for _ in range(size)]

    def add_edge(u, v, capacity, cost):
        graph[u].append([v, len(graph[v]), capacity, cost])
        graph[v].append([u, len(graph[u]) - 1, 0, -cost])

    for node, c in enumerate(letters, 1):
        add_edge(source, node, counts[c], 0)
        for i in range(half):
            j = n - 1 - i
            gain = 0
            if s[i] - 97 == c:
                gain = beauty[i]
            if s[j] - 97 == c:
                gain = max(gain, beauty[j])
            add_edge(node, pair_start + i, 1, -gain)

    potential = [0] * size
    for i in range(half):
        node = pair_start + i
        add_edge(node, sink, 2, 0)
        potential[node] = -max(beauty[i], beauty[n - 1 - i])
    potential[sink] = -max(beauty)

    total_cost = 0
    flow = 0
    inf = 10**18

    while flow < n:
        dist = [inf] * size
        previous_node = [-1] * size
        previous_edge = [-1] * size
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for ei, edge in enumerate(graph[u]):
                v, _, capacity, cost = edge
                if capacity:
                    nd = d + cost + potential[u] - potential[v]
                    if nd < dist[v]:
                        dist[v] = nd
                        previous_node[v] = u
                        previous_edge[v] = ei
                        heapq.heappush(heap, (nd, v))

        for v in range(size):
            if dist[v] < inf:
                potential[v] += dist[v]

        amount = n - flow
        v = sink
        while v != source:
            u = previous_node[v]
            edge = graph[u][previous_edge[v]]
            amount = min(amount, edge[2])
            v = u

        v = sink
        while v != source:
            u = previous_node[v]
            edge = graph[u][previous_edge[v]]
            total_cost += amount * edge[3]
            edge[2] -= amount
            graph[v][edge[1]][2] += amount
            v = u

        flow += amount

    print(-total_cost)


if __name__ == "__main__":
    main()
