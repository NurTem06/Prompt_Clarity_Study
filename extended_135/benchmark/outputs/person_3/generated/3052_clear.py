import sys
import math
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    ax, ay, bx, by = map(float, data[:4])
    n = int(data[4])

    anchors = [(ax, ay), (bx, by)]
    conveyors = []
    pos = 5

    for _ in range(n):
        x1, y1, x2, y2 = map(float, data[pos:pos + 4])
        pos += 4
        start_id = len(anchors)
        anchors.append((x1, y1))
        end_id = len(anchors)
        anchors.append((x2, y2))
        length = math.hypot(x2 - x1, y2 - y1)
        conveyors.append((
            x1, y1, (x2 - x1) / length, (y2 - y1) / length,
            length, start_id, end_id
        ))

    count = len(anchors)
    graph = [[] for _ in range(count)]
    hypot = math.hypot

    for i in range(count):
        x, y = anchors[i]
        for j in range(i):
            xx, yy = anchors[j]
            distance = hypot(x - xx, y - yy)
            graph[i].append((j, distance))
            graph[j].append((i, distance))

    inv_sqrt3 = 1.0 / math.sqrt(3.0)

    for sx, sy, ux, uy, length, start_id, end_id in conveyors:
        nodes = {0.0: start_id, length: end_id}

        for anchor_id, (x, y) in enumerate(anchors):
            if anchor_id == start_id or anchor_id == end_id:
                continue

            dx = x - sx
            dy = y - sy
            projection = dx * ux + dy * uy
            perpendicular = abs(dx * uy - dy * ux)
            offset = perpendicular * inv_sqrt3

            entry = max(0.0, min(length, projection + offset))
            node_id = nodes.get(entry)
            if node_id is None:
                node_id = len(graph)
                graph.append([])
                nodes[entry] = node_id
            graph[anchor_id].append((
                node_id, hypot(entry - projection, perpendicular)
            ))

            exit_position = max(0.0, min(length, projection - offset))
            node_id = nodes.get(exit_position)
            if node_id is None:
                node_id = len(graph)
                graph.append([])
                nodes[exit_position] = node_id
            graph[node_id].append((
                anchor_id, hypot(exit_position - projection, perpendicular)
            ))

        ordered = sorted(nodes.items())
        previous_position, previous_id = ordered[0]
        for current_position, current_id in ordered[1:]:
            graph[previous_id].append((
                current_id, (current_position - previous_position) * 0.5
            ))
            previous_position = current_position
            previous_id = current_id

    distances = [math.inf] * len(graph)
    distances[0] = 0.0
    heap = [(0.0, 0)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance != distances[node]:
            continue
        if node == 1:
            print(f"{distance:.12f}")
            return

        for neighbor, weight in graph[node]:
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))


if __name__ == "__main__":
    main()
