import sys


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = []
    left, right = intervals[0]
    for lo, hi in intervals[1:]:
        if lo <= right + 1:
            if hi > right:
                right = hi
        else:
            merged.append((left, right))
            left, right = lo, hi
    merged.append((left, right))
    return merged


def feasible(groups, require_service):
    remaining = [(0, 20000 - groups[0][3])]

    for i in range(1, len(groups)):
        previous = groups[i - 1]
        current = groups[i]
        gap = current[0] - previous[0]

        if require_service and gap > 12:
            return False

        intermediate_min = 2000 * (gap - 1)
        intermediate_max = 20000 * (gap - 1)
        offset_max = 20000 - current[3]
        residue = (current[1] - previous[2]) % 100000
        candidates = []

        for lo, hi in remaining:
            minimum_distance = lo + intermediate_min
            maximum_distance = hi + intermediate_max + offset_max

            if require_service:
                maximum_distance = min(maximum_distance, 30000)

            first_wrap = max(0, (minimum_distance - residue + 99999) // 100000)
            last_wrap = (maximum_distance - residue) // 100000

            for wraps in range(first_wrap, last_wrap + 1):
                distance = residue + 100000 * wraps
                offset_lo = max(0, distance - hi - intermediate_max)
                offset_hi = min(offset_max, distance - lo - intermediate_min)

                if offset_lo <= offset_hi:
                    remaining_lo = max(0, 2000 - current[3] - offset_hi)
                    remaining_hi = 20000 - current[3] - offset_lo
                    candidates.append((remaining_lo, remaining_hi))

        remaining = merge_intervals(candidates)
        if not remaining:
            return False

    return True


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    count = data[0]
    groups = []
    impossible = False

    for i in range(count):
        year, month, odometer = data[1 + 3 * i:4 + 3 * i]
        date = year * 12 + month - 1

        if groups and groups[-1][0] == date:
            group = groups[-1]
            group[3] += (odometer - group[2]) % 100000
            group[2] = odometer
            if group[3] > 20000:
                impossible = True
        else:
            groups.append([date, odometer, odometer, 0])

    if impossible or not feasible(groups, False):
        print("tampered odometer")
    elif not feasible(groups, True):
        print("insufficient service")
    else:
        print("seems legit")


if __name__ == "__main__":
    main()
