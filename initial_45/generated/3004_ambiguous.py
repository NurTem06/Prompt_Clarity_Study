import sys
from bisect import bisect_left


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    groups = {}
    offers = []
    endpoints = {0, 10000}

    pos = 1
    for _ in range(n):
        color = data[pos]
        a = int(data[pos + 1])
        b = int(data[pos + 2])
        pos += 3
        if color not in groups:
            groups[color] = []
        groups[color].append((a, b))
        offers.append((a, b, color))
        endpoints.add(b)

    offers.sort()
    covered = 0
    index = 0
    lower = 0
    used_colors = set()

    while covered < 10000:
        farthest = covered
        chosen_color = None
        while index < n and offers[index][0] <= covered + 1:
            _, b, color = offers[index]
            if b > farthest:
                farthest = b
                chosen_color = color
            index += 1
        if farthest == covered:
            print("IMPOSSIBLE")
            return
        covered = farthest
        lower += 1
        used_colors.add(chosen_color)

    if len(used_colors) <= 3:
        print(lower)
        return

    points = sorted(endpoints)
    target = len(points) - 1
    endpoint_index = {value: i for i, value in enumerate(points)}

    rows = []
    flags = []
    counts = []

    for intervals in groups.values():
        intervals.sort()
        useful = []
        farthest = 0
        for a, b in intervals:
            if b > farthest:
                useful.append((a, b))
                farthest = b

        flag = 0
        if intervals[0][0] == 1:
            flag |= 1
        if farthest == 10000:
            flag |= 2

        row = []
        j = 0
        reach = 0
        for p, value in enumerate(points):
            while j < len(useful) and useful[j][0] <= value + 1:
                reach = endpoint_index[useful[j][1]]
                j += 1
            row.append(max(p, reach))

        rows.append(row)
        flags.append(flag)
        counts.append(len(useful))

    k = len(rows)
    best = n + 1

    for i in range(k):
        if flags[i] != 3 or counts[i] < lower:
            continue
        row = rows[i]
        p = 0
        steps = 0
        while p < target and steps < best:
            q = row[p]
            if q == p:
                break
            p = q
            steps += 1
        if p == target and steps < best:
            best = steps
            if best == lower:
                print(best)
                return

    for i in range(k):
        a = rows[i]
        for j in range(i + 1, k):
            if (flags[i] | flags[j]) != 3:
                continue
            if counts[i] + counts[j] < lower:
                continue
            b = rows[j]
            p = 0
            steps = 0
            while p < target and steps < best:
                q = a[p]
                if b[p] > q:
                    q = b[p]
                if q == p:
                    break
                p = q
                steps += 1
            if p == target and steps < best:
                best = steps
                if best == lower:
                    print(best)
                    return

    for i in range(k - 2):
        a = rows[i]
        fi = flags[i]
        ni = counts[i]
        for j in range(i + 1, k - 1):
            b = rows[j]
            pair_flags = fi | flags[j]
            pair_count = ni + counts[j]
            first = max(a[0], b[0])

            for h in range(j + 1, k):
                if (pair_flags | flags[h]) != 3:
                    continue
                if pair_count + counts[h] < lower:
                    continue

                c = rows[h]
                p = first
                if c[0] > p:
                    p = c[0]
                steps = 1

                while p < target and steps < best:
                    q = a[p]
                    if b[p] > q:
                        q = b[p]
                    if c[p] > q:
                        q = c[p]
                    if q == p:
                        break
                    p = q
                    steps += 1

                if p == target and steps < best:
                    best = steps
                    if best == lower:
                        print(best)
                        return

    print(best if best <= n else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
