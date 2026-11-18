import sys
import math
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    ax, ay, bx, by = map(float, data[:4])
    n = int(data[4])

    if n == 0:
        print(f"{math.hypot(ax - bx, ay - by):.10f}")
        return

    points = [(ax, ay), (bx, by)]
    belts = []
    pos = 5

    for _ in range(n):
        x1, y1, x2, y2 = map(float, data[pos:pos + 4])
        pos += 4
        start = len(points)
        points.append((x1, y1))
        points.append((x2, y2))
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        belts.append((x1, y1, dx / length, dy / length, length, start))

    base_count = len(points)
    graph = [[] for _ in range(base_count)]

    for i in range(base_count):
        x, y = points[i]
        for j in range(i):
            xx, yy = points[j]
            distance = math.hypot(x - xx, y - yy)
            graph[i].append((j, distance))
            graph[j].append((i, distance))

    inv_sqrt3 = 1.0 / math.sqrt(3.0)

    for x, y, ux, uy, length, start in belts:
        ordered = [(0.0, start), (length, start + 1)]

        for p, (px, py) in enumerate(points):
            if p == start or p == start + 1:
                continue

            dx, dy = px - x, py - y
            projection = dx * ux + dy * uy
            offset = abs(dx * uy - dy * ux) * inv_sqrt3
            walk_time = 2.0 * offset

            boarding = projection + offset
            if 0.0 < boarding < length:
                node = len(graph)
                graph.append([])
                graph[p].append((node, walk_time))
                ordered.append((boarding, node))

            leaving = projection - offset
            if 0.0 < leaving < length:
                node = len(graph)
                graph.append([(p, walk_time)])
                ordered.append((leaving, node))

        ordered.sort()
        previous_t, previous_node = ordered[0]
        for t, node in ordered[1:]:
            graph[previous_node].append((node, (t - previous_t) * 0.5))
            previous_t, previous_node = t, node

    distances = [math.inf] * len(graph)
    distances[0] = 0.0
    heap = [(0.0, 0)]
    pop = heapq.heappop
    push = heapq.heappush

    while heap:
        distance, node = pop(heap)
        if distance != distances[node]:
            continue
        if node == 1:
            print(f"{distance:.10f}")
            return
        for nxt, weight in graph[node]:
            candidate = distance + weight
            if candidate < distances[nxt]:
                distances[nxt] = candidate
                push(heap, (candidate, nxt))


if __name__ == "__main__":
    main()
