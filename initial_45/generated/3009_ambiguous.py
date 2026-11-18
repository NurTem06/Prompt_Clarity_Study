import sys
import math
import heapq


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    lamps = [tuple(data[j:j + 3]) for j in range(1, 3 * n + 1, 3)]
    lamps.sort()

    total = sum(p[2] for p in lamps)
    if total % 2:
        print("IMPOSSIBLE")
        return

    target = total // 2
    if target == 0:
        print("0")
        return

    size = 1 << n
    sums = [0] * size
    goals = [[] for _ in range(n)]
    for mask in range(1, size):
        bit = mask & -mask
        index = bit.bit_length() - 1
        sums[mask] = sums[mask ^ bit] + lamps[index][2]
        if sums[mask] == target:
            goals[index].append(mask >> index)

    if not any(goals):
        print("IMPOSSIBLE")
        return

    if any(e == target for _, _, e in lamps):
        print("8")
        return

    points = sorted({
        (x + dx, y + dy)
        for x, y, _ in lamps
        for dx in (-1, 1)
        for dy in (-1, 1)
    })
    count = len(points)
    point_index = {p: i for i, p in enumerate(points)}
    graph = [[] for _ in points]

    for a in range(count):
        ax, ay = points[a]
        for b in range(a + 1, count):
            bx, by = points[b]
            dx = bx - ax
            dy = by - ay
            visible = True

            for x, y, _ in lamps:
                if dx == 0:
                    if not x - 1 < ax < x + 1:
                        continue
                    lo = 0.0
                    hi = 1.0
                else:
                    t1 = (x - 1 - ax) / dx
                    t2 = (x + 1 - ax) / dx
                    if t1 > t2:
                        t1, t2 = t2, t1
                    lo = max(0.0, t1)
                    hi = min(1.0, t2)
                    if lo >= hi - 1e-12:
                        continue

                if dy == 0:
                    if not y - 1 < ay < y + 1:
                        continue
                else:
                    t1 = (y - 1 - ay) / dy
                    t2 = (y + 1 - ay) / dy
                    if t1 > t2:
                        t1, t2 = t2, t1
                    lo = max(lo, t1)
                    hi = min(hi, t2)

                if lo < hi - 1e-12:
                    visible = False
                    break

            if not visible:
                continue

            crossing = 0
            if dy:
                for k, (x, y, _) in enumerate(lamps):
                    ray_y = y + 0.5
                    if (ay < ray_y) != (by < ray_y):
                        cross_x = ax + dx * ((ray_y - ay) / dy)
                        if cross_x < x:
                            crossing |= 1 << k

            length = math.hypot(dx, dy)
            graph[a].append((b, length, crossing))
            graph[b].append((a, length, crossing))

    best = math.inf
    heappush = heapq.heappush
    heappop = heapq.heappop

    order = [i for i in range(n) if goals[i]]
    order.sort(key=lambda i: (len(goals[i]), -i))

    for i in order:
        x, y, _ = lamps[i]
        start = point_index[(x - 1, y - 1)]
        upper = point_index[(x - 1, y + 1)]

        allowed = [p >= (x - 1, y - 1) for p in points]
        lower_bits = (1 << i) - 1
        adjacency = [[] for _ in points]

        initial_mask = None
        for v, length, mask in graph[start]:
            if v == upper:
                initial_mask = mask >> i
                break
        if initial_mask is None:
            continue

        for u in range(count):
            if not allowed[u]:
                continue
            row = adjacency[u]
            for v, length, mask in graph[u]:
                if allowed[v] and not (mask & lower_bits):
                    row.append((v, length, (mask >> i) << 6))

        goal = bytearray(1 << (n - i))
        for mask in goals[i]:
            goal[mask] = 1

        distances = [math.inf] * ((1 << (n - i)) << 6)
        initial_state = (initial_mask << 6) | upper
        distances[initial_state] = 2.0
        heap = [(2.0, initial_state)]

        while heap:
            distance, state = heappop(heap)
            if distance != distances[state]:
                continue
            if distance >= best:
                break

            vertex = state & 63
            mask_part = state & ~63

            if vertex == start and goal[state >> 6]:
                best = distance
                break

            for neighbor, length, edge_mask in adjacency[vertex]:
                new_distance = distance + length
                if new_distance >= best:
                    continue
                new_state = (mask_part ^ edge_mask) | neighbor
                if new_distance < distances[new_state]:
                    distances[new_state] = new_distance
                    heappush(heap, (new_distance, new_state))

    if math.isinf(best):
        print("IMPOSSIBLE")
    else:
        print(f"{best:.12f}")


if __name__ == "__main__":
    main()
