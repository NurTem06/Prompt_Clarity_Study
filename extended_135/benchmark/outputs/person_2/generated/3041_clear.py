import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    if n == 0:
        print(0)
        return

    dp = [0] * (n + 1)
    ranges = []
    previous_zone = 0
    left = 0

    for i in range(1, n + 1):
        zone = data[2 * i - 1]
        time = data[2 * i]

        while time - data[2 * left + 2] >= 10000:
            left += 1

        updated = []
        best = dp[i - 1] + abs(zone - previous_zone) + 2
        count = len(ranges)

        for j in range(count):
            low, high, start = ranges[j]
            end = ranges[j + 1][2] if j + 1 < count else i - 1

            if end <= left:
                continue

            if start < left:
                start = left
            if zone < low:
                low = zone
            if zone > high:
                high = zone

            if updated and updated[-1][0] == low and updated[-1][1] == high:
                continue

            updated.append((low, high, start))
            candidate = dp[start] + high - low + 2
            if candidate < best:
                best = candidate

        if previous_zone < zone:
            low, high = previous_zone, zone
        else:
            low, high = zone, previous_zone

        if not updated or updated[-1][0] != low or updated[-1][1] != high:
            updated.append((low, high, i - 1))

        dp[i] = best
        ranges = updated
        previous_zone = zone

    print(dp[n])


if __name__ == "__main__":
    main()
