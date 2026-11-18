import sys


def main():
    read = sys.stdin.buffer.readline
    d, t, c, r = map(int, read().split())

    diff = [0] * (t + 1)
    for _ in range(c):
        s, e, p, a = read().split()
        amount = int(round(float(p) * 1000000)) * int(a)
        diff[int(s)] += amount
        diff[int(e)] -= amount

    roofs = []
    for _ in range(r):
        x, y = map(int, read().split())
        roofs.append((x, min(y, d)))
    roofs.sort()

    gaps = []
    position = 0
    for x, y in roofs:
        if x > position:
            gaps.append((position, x))
        if y > position:
            position = y
    if position < d:
        gaps.append((position, d))

    if not gaps:
        print("0.0")
        return

    prefix = [0] * (t + 1)
    intensity = 0
    total = 0
    for i in range(t):
        intensity += diff[i]
        total += intensity
        prefix[i + 1] = total

    width = t - d + 1
    dp = [0] * width

    for start, end in gaps:
        best = None
        for delay in range(width):
            value = dp[delay] + prefix[end + delay] - prefix[start + delay]
            if best is None or value < best:
                best = value
            dp[delay] = best

    answer = dp[-1]
    print(f"{answer // 1000000}.{answer % 1000000:06d}")


if __name__ == "__main__":
    main()
