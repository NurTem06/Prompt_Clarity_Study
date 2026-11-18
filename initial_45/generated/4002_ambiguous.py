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

    total = [-1] * k
    total[0] = 0
    pos = 3

    for _ in range(n):
        dp = [[-1] * k for _ in range(limit + 1)]
        dp[0][0] = 0

        for j in range(m):
            value = data[pos]
            pos += 1
            shift = value % k

            for count in range(min(j, limit - 1), -1, -1):
                source = dp[count]
                target = dp[count + 1]
                for remainder, current in enumerate(source):
                    if current < 0:
                        continue
                    new_remainder = remainder + shift
                    if new_remainder >= k:
                        new_remainder -= k
                    candidate = current + value
                    if candidate > target[new_remainder]:
                        target[new_remainder] = candidate

        best = [-1] * k
        for states in dp:
            for remainder, value in enumerate(states):
                if value > best[remainder]:
                    best[remainder] = value

        options = [(r, value) for r, value in enumerate(best) if value >= 0]
        merged = [-1] * k
        for remainder, current in enumerate(total):
            if current < 0:
                continue
            for row_remainder, row_value in options:
                new_remainder = remainder + row_remainder
                if new_remainder >= k:
                    new_remainder -= k
                candidate = current + row_value
                if candidate > merged[new_remainder]:
                    merged[new_remainder] = candidate
        total = merged

    print(total[0])


if __name__ == "__main__":
    main()