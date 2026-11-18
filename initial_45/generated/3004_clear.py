import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    offers = []
    groups = {}
    boundaries = {1, 10001}
    endpoints = {0}

    p = 1
    for _ in range(n):
        color = data[p]
        a = int(data[p + 1])
        b = int(data[p + 2])
        p += 3
        offers.append((a, b, color))
        groups.setdefault(color, []).append((a, b))
        boundaries.add(a)
        boundaries.add(b + 1)
        endpoints.add(b)

    offers.sort()
    pos = 0
    idx = 0
    lower = 0
    chosen_colors = set()

    while pos < 10000:
        far = pos
        far_color = None
        while idx < n and offers[idx][0] <= pos + 1:
            _, b, color = offers[idx]
            if b > far:
                far = b
                far_color = color
            idx += 1
        if far == pos:
            print("IMPOSSIBLE")
            return
        pos = far
        lower += 1
        chosen_colors.add(far_color)

    if lower <= 3 or len(chosen_colors) <= 3 or len(groups) <= 3:
        print(lower)
        return

    boundaries = sorted(boundaries)
    boundary_index = {v: i for i, v in enumerate(boundaries)}
    full_mask = (1 << (len(boundaries) - 1)) - 1

    states = sorted(endpoints)
    state_index = {v: i for i, v in enumerate(states)}
    target = state_index[10000]

    colors = []
    for intervals in groups.values():
        intervals.sort()
        mask = 0
        for a, b in intervals:
            left = boundary_index[a]
            right = boundary_index[b + 1]
            mask |= ((1 << (right - left)) - 1) << left

        transitions = []
        j = 0
        far = 0
        length = len(intervals)
        for end in states:
            while j < length and intervals[j][0] <= end + 1:
                if intervals[j][1] > far:
                    far = intervals[j][1]
                j += 1
            transitions.append(state_index[far])

        colors.append((mask, transitions))

    colors.sort(key=lambda item: item[0].bit_count(), reverse=True)
    masks = [item[0] for item in colors]
    reaches = [item[1] for item in colors]
    count = len(colors)
    best = n + 1

    for i in range(count - 2):
        mask_i = masks[i]
        reach_i = reaches[i]
        for j in range(i + 1, count - 1):
            pair_mask = mask_i | masks[j]
            pair_reach = None

            for k in range(j + 1, count):
                if pair_mask | masks[k] != full_mask:
                    continue

                if pair_reach is None:
                    pair_reach = [
                        a if a >= b else b
                        for a, b in zip(reach_i, reaches[j])
                    ]

                third_reach = reaches[k]
                state = 0
                used = 0

                while state != target and used < best:
                    a = pair_reach[state]
                    b = third_reach[state]
                    state = a if a >= b else b
                    used += 1

                if state == target and used < best:
                    best = used
                    if best == lower:
                        print(best)
                        return

    print(best if best <= n else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
