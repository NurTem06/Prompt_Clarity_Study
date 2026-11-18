import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data or data[0] == 0:
        print(0)
        return

    n = data[0]
    dp = [0] * (n + 1)
    times = [0] * n
    last = [-1] * 11
    last[0] = 0
    order = [0]
    left = 0

    for i in range(1, n + 1):
        zone = data[2 * i - 1]
        time = data[2 * i]
        times[i - 1] = time

        while times[left] + 10000 <= time:
            left += 1

        if last[zone] >= 0:
            order.remove(zone)
        order.insert(0, zone)
        last[zone] = i

        low = 11
        high = -1
        best = dp[i - 1] + abs(zone - (data[2 * i - 3] if i > 1 else 0)) + 2
        count = len(order)

        for j in range(count):
            current = order[j]
            position = last[current]
            if position < left:
                break

            if current < low:
                low = current
            if current > high:
                high = current

            next_position = last[order[j + 1]] if j + 1 < count else -1
            start = max(left, next_position + 1)

            if start < i:
                candidate = dp[start] + high - low + 2
                if candidate < best:
                    best = candidate

            if next_position < left:
                break

        dp[i] = best

    print(dp[n])


if __name__ == "__main__":
    main()