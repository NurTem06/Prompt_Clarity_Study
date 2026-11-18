import sys
import math
import heapq


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    lamps = sorted(tuple(data[i:i + 3]) for i in range(1, 3 * n + 1, 3))
    total = sum(p[2] for p in lamps)

    if total % 2:
        print("IMPOSSIBLE")
        return
    if total == 0:
        print("0")
        return

    size = 1 << n
    target = total // 2
    sums = [0] * size
    balanced = bytearray(size)
    active = [False] * n

    for mask in range(1, size):
        bit = mask & -mask
        i = bit.bit_length() - 1
        sums[mask] = sums[mask ^ bit] + lamps[i][2]
        if sums[mask] == target:
            balanced[mask] = 1
            active[i] = True

    if not any(active):
        print("IMPOSSIBLE")
        return

    points = sorted({
        (x + dx, y + dy)
        for x, y, _ in lamps
        for dx in (-1, 1)
        for dy in (-1, 1)
    })
    index = {p: i for i, p in enumerate(points)}
    count = len(points)
    graph = [[] for _ in points]

    for a in range(count):
        ax, ay = points[a]
        for b in range(a + 1, count):
            bx, by = points[b]
            dx = bx - ax
            dy = by - ay
            blocked = False

            for x, y, _ in lamps:
                lo = 0.0
                hi = 1.0

                if dx == 0:
                    if not x - 1 < ax < x + 1:
                        continue
                else:
                    t1 = (x - 1 - ax) / dx
                    t2 = (x + 1 - ax) / dx
                    if t1 > t2:
                        t1, t2 = t2, t1
                    lo = max(lo, t1)
                    hi = min(hi, t2)

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
                    blocked = True
                    break

            if blocked:
                continue

            crossing = 0
            if dy:
                for k, (x, y, _) in enumerate(lamps):
                    if (ay <= y < by) or (by <= y < ay):
                        cross = (ax - x) * dy + (y - ay) * dx
                        if (cross < 0) if dy > 0 else (cross > 0):
                            crossing |= 1 << k

            length = math.hypot(dx, dy)
            shifted = crossing << 6
            graph[a].append((b, length, shifted))
            graph[b].append((a, length, shifted))

    best = math.inf
    state_count = size << 6
    heappush = heapq.heappush
    heappop = heapq.heappop

    for lamp_id in range(n - 1, -1, -1):
        if not active[lamp_id]:
            continue

        x, y, _ = lamps[lamp_id]
        start = index[(x - 1, y - 1)]
        sx, sy = points[start]
        heuristic = [
            math.hypot(px - sx, py - sy) for px, py in points
        ]

        edges = [[] for _ in points]
        for v in range(start, count):
            edges[v] = [
                (w, length, toggle)
                for w, length, toggle in graph[v]
                if w >= start
            ]

        dist = [math.inf] * state_count
        dist[start] = 0.0
        heap = [(0.0, 0.0, start)]
        first_bit = 1 << lamp_id
        lower_bits = (first_bit << 1) - 1

        while heap:
            estimate, distance, state = heappop(heap)
            if estimate >= best:
                break
            if distance != dist[state]:
                continue

            v = state & 63
            mask = state >> 6
            if (
                v == start
                and balanced[mask]
                and mask & lower_bits == first_bit
            ):
                best = distance
                break

            base = state ^ v
            for w, length, toggle in edges[v]:
                nd = distance + length
                ne = nd + heuristic[w]
                if ne >= best:
                    continue
                ns = (base ^ toggle) | w
                if nd < dist[ns]:
                    dist[ns] = nd
                    heappush(heap, (ne, nd, ns))

    if math.isinf(best):
        print("IMPOSSIBLE")
    else:
        print(f"{best:.12f}")


if __name__ == "__main__":
    main()
