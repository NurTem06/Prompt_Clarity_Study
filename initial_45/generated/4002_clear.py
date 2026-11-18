import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[:3]
    limit = m // 2

    if limit == 0:
        print(0)
        return

    if k == 1:
        print(sum(
            sum(sorted(data[3 + i * m:3 + (i + 1) * m], reverse=True)[:limit])
            for i in range(n)
        ))
        return

    shifts = [[(r + v) % k for r in range(k)] for v in range(k)]
    total = [-1] * k
    total[0] = 0
    pos = 3

    for _ in range(n):
        row = data[pos:pos + m]
        pos += m

        dp = [[-1] * k for _ in range(limit + 1)]
        dp[0][0] = 0

        for index, value in enumerate(row):
            shift = shifts[value % k]
            for count in range(min(index, limit - 1), -1, -1):
                source = dp[count]
                target = dp[count + 1]
                for remainder, current in enumerate(source):
                    if current >= 0:
                        new_remainder = shift[remainder]
                        candidate = current + value
                        if candidate > target[new_remainder]:
                            target[new_remainder] = candidate

        best = [-1] * k
        for state in dp:
            for remainder, value in enumerate(state):
                if value > best[remainder]:
                    best[remainder] = value

        combined = [-1] * k
        available = [(r, value) for r, value in enumerate(best) if value >= 0]
        for remainder, current in enumerate(total):
            if current < 0:
                continue
            shift = shifts[remainder]
            for row_remainder, value in available:
                new_remainder = shift[row_remainder]
                candidate = current + value
                if candidate > combined[new_remainder]:
                    combined[new_remainder] = candidate
        total = combined

    print(total[0])


if __name__ == "__main__":
    main()
