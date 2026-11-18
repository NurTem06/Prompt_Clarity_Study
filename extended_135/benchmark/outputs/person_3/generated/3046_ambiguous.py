import sys
from bisect import bisect_left


def fail():
    sys.stdout.write("syntax error\n")
    raise SystemExit


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    try:
        n = next(data)
    except StopIteration:
        return

    top = [(next(data), next(data)) for _ in range(n)]
    bottom = [(next(data), next(data)) for _ in range(n)]
    del data

    events = [(r, c, 0, i) for i, (r, c) in enumerate(top)]
    events.extend((r, c, 1, i) for i, (r, c) in enumerate(bottom))
    events.sort()

    columns = sorted({c for _, c in top})
    m = len(columns)
    ranks = {c: i + 1 for i, c in enumerate(columns)}
    bit = [0] * (m + 1)
    active = [-1] * (m + 1)
    answer = [-1] * n
    highest_bit = 1 << (m.bit_length() - 1)

    for r, c, kind, identifier in events:
        if kind == 0:
            index = ranks[c]
            if active[index] != -1:
                fail()
            active[index] = identifier
            p = index
            while p <= m:
                bit[p] += 1
                p += p & -p
        else:
            p = bisect_left(columns, c)
            count = 0
            while p:
                count += bit[p]
                p -= p & -p
            if count == 0:
                fail()

            position = 0
            step = highest_bit
            while step:
                candidate = position + step
                if candidate <= m and bit[candidate] < count:
                    count -= bit[candidate]
                    position = candidate
                step >>= 1

            index = position + 1
            opening = active[index]
            if opening == -1 or top[opening][0] >= r:
                fail()

            answer[opening] = identifier
            active[index] = -1
            p = index
            while p <= m:
                bit[p] -= 1
                p += p & -p

    del events, bit, active, ranks, columns

    columns = sorted({c for _, c in top} | {c for _, c in bottom})
    ranks = {c: i + 1 for i, c in enumerate(columns)}
    m = len(columns)
    events = []

    for i, (r1, c1) in enumerate(top):
        j = answer[i]
        if j < 0:
            fail()
        r2, c2 = bottom[j]
        left = ranks[c1]
        right = ranks[c2]
        events.append((r1, left, right, 1))
        events.append((r2, left, right, -1))

    events.sort()
    bit = [0] * (m + 1)
    previous_row = -1
    previous_right = -1

    for row, left, right, change in events:
        if row == previous_row and left <= previous_right:
            fail()
        previous_row = row
        previous_right = right

        count = 0
        p = right
        while p:
            count += bit[p]
            p -= p & -p
        p = left - 1
        while p:
            count -= bit[p]
            p -= p & -p

        if count != (0 if change == 1 else 2):
            fail()

        p = left
        while p <= m:
            bit[p] += change
            p += p & -p
        p = right
        while p <= m:
            bit[p] += change
            p += p & -p

    sys.stdout.write("\n".join(str(j + 1) for j in answer) + "\n")


if __name__ == "__main__":
    main()
