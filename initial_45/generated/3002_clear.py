import sys


def feasible(entries, sufficient_service):
    intervals = [(0, 20000)]

    for i in range(1, len(entries)):
        previous_month, previous_reading = entries[i - 1]
        month, reading = entries[i]
        gap = month - previous_month
        distance = (reading - previous_reading) % 100000

        if sufficient_service and (gap > 12 or distance > 30000):
            return False

        possible = []

        if gap == 0:
            for low, high in intervals:
                new_low = low + distance
                new_high = min(20000, high + distance)
                if new_low <= new_high:
                    possible.append((new_low, new_high))
        else:
            middle_min = 2000 * (gap - 1)
            middle_max = 20000 * (gap - 1)

            for low, high in intervals:
                remaining_min = max(0, 2000 - high)
                remaining_max = 20000 - low

                minimum_distance = remaining_min + middle_min
                maximum_distance = remaining_max + middle_max + 20000

                if sufficient_service:
                    first_wrap = last_wrap = 0
                else:
                    first_wrap = max(
                        0, (minimum_distance - distance + 99999) // 100000
                    )
                    last_wrap = (maximum_distance - distance) // 100000

                for wraps in range(first_wrap, last_wrap + 1):
                    traveled = distance + 100000 * wraps
                    new_low = max(
                        0, traveled - remaining_max - middle_max
                    )
                    new_high = min(
                        20000, traveled - remaining_min - middle_min
                    )
                    if new_low <= new_high:
                        possible.append((new_low, new_high))

        if not possible:
            return False

        possible.sort()
        intervals = []
        low, high = possible[0]
        for next_low, next_high in possible[1:]:
            if next_low <= high:
                high = max(high, next_high)
            else:
                intervals.append((low, high))
                low, high = next_low, next_high
        intervals.append((low, high))

    return True


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    count = data[0]
    entries = []
    for i in range(count):
        year, month, reading = data[1 + 3 * i:4 + 3 * i]
        entries.append((year * 12 + month - 1, reading))

    if not feasible(entries, False):
        print("tampered odometer")
    elif not feasible(entries, True):
        print("insufficient service")
    else:
        print("seems legit")


if __name__ == "__main__":
    main()
