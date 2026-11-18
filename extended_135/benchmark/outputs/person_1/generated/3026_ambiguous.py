import sys
from bisect import bisect_left


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:n + 1]

    left = [0] * n
    tails = []
    for i, value in enumerate(a):
        pos = bisect_left(tails, value)
        if pos == len(tails):
            tails.append(value)
        else:
            tails[pos] = value
        left[i] = pos + 1

    lis_length = len(tails)
    counts = [0] * (lis_length + 1)
    candidates = [0] * (lis_length + 1)

    tails = []
    for i in range(n - 1, -1, -1):
        value = -a[i]
        pos = bisect_left(tails, value)
        if pos == len(tails):
            tails.append(value)
        else:
            tails[pos] = value

        if left[i] + pos == lis_length:
            level = left[i]
            counts[level] += 1
            candidates[level] = a[i]

    answer = sorted(
        candidates[level]
        for level in range(1, lis_length + 1)
        if counts[level] == 1
    )
    sys.stdout.write(" ".join(map(str, answer)) if answer else "-1")


if __name__ == "__main__":
    main()
