import sys
from bisect import bisect_left


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:n + 1]

    tails = []
    left = [0] * n
    for i, x in enumerate(a):
        p = bisect_left(tails, x)
        if p == len(tails):
            tails.append(x)
        else:
            tails[p] = x
        left[i] = p + 1

    length = len(tails)
    counts = [0] * (length + 1)
    candidates = [0] * (length + 1)
    tails = []

    for i in range(n - 1, -1, -1):
        x = a[i]
        p = bisect_left(tails, -x)
        if p == len(tails):
            tails.append(-x)
        else:
            tails[p] = -x

        rank = left[i]
        if rank + p == length:
            counts[rank] += 1
            candidates[rank] = x

    answer = sorted(
        candidates[rank]
        for rank in range(1, length + 1)
        if counts[rank] == 1
    )
    print(" ".join(map(str, answer)) if answer else "-1")


if __name__ == "__main__":
    main()
