import sys


def main():
    read = sys.stdin.buffer.readline
    d, t, c, r = map(int, read().split())

    diff = [0] * (t + 1)
    for _ in range(c):
        s, e, p, a = read().split()
        amount = int(float(p) * 1_000_000 + 0.5) * int(a)
        diff[int(s)] += amount
        diff[int(e)] -= amount

    rain = [0] * t
    current = 0
    for i in range(t):
        current += diff[i]
        rain[i] = current

    covered = bytearray(d)
    sheltered = bytearray(d + 1)
    sheltered[0] = 1

    for _ in range(r):
        x, y = map(int, read().split())
        end = min(y, d)
        covered[x:end] = b'\x01' * (end - x)
        sheltered[x:end + 1] = b'\x01' * (end - x + 1)

    slack = t - d
    dp = [0] * (slack + 1)
    indices = range(1, slack + 1)

    for x in range(1, d + 1):
        offset = x - 1

        if covered[offset]:
            continue

        best = dp[0] + rain[offset]
        dp[0] = best

        if sheltered[x]:
            for k in indices:
                value = dp[k] + rain[offset + k]
                if value < best:
                    best = value
                dp[k] = best
        else:
            for k in indices:
                value = dp[k]
                if best < value:
                    value = best
                best = value + rain[offset + k]
                dp[k] = best

    answer = min(dp)
    whole, fraction = divmod(answer, 1_000_000)
    print(f"{whole}.{fraction:06d}")


if __name__ == "__main__":
    main()