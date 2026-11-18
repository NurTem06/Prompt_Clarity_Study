import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    columns = sorted(set(data[2::2]))
    rank = {c: i + 1 for i, c in enumerate(columns)}
    m = len(columns)

    top_rows = [0] * n
    top_cols = [0] * n
    events = []

    p = 1
    for i in range(n):
        r = data[p]
        c = rank[data[p + 1]]
        p += 2
        top_rows[i] = r
        top_cols[i] = c
        events.append((r, c, i + 1))

    for i in range(n):
        r = data[p]
        c = rank[data[p + 1]]
        p += 2
        events.append((r, c, -i - 1))

    del data, rank, columns
    events.sort()

    bit = [0] * (m + 1)
    heads = [-1] * (m + 1)
    previous = [-1] * n
    answer = [0] * n
    checks = []
    highest_bit = 1 << (m.bit_length() - 1)

    for row, col, ident in events:
        if ident > 0:
            idx = ident - 1
            previous[idx] = heads[col]
            heads[col] = idx
            k = col
            while k <= m:
                bit[k] += 1
                k += k & -k
        else:
            count = 0
            k = col
            while k:
                count += bit[k]
                k -= k & -k

            if count == 0:
                sys.stdout.write("syntax error\n")
                return

            pos = 0
            step = highest_bit
            while step:
                nxt = pos + step
                if nxt <= m and bit[nxt] < count:
                    count -= bit[nxt]
                    pos = nxt
                step >>= 1
            left = pos + 1

            idx = heads[left]
            heads[left] = previous[idx]
            answer[idx] = -ident

            k = left
            while k <= m:
                bit[k] -= 1
                k += k & -k

            checks.append((top_rows[idx], 0, left, col))
            checks.append((row, 1, left, col))

    del events, heads, previous, top_rows, top_cols
    checks.sort()

    total = len(checks)
    start = 0
    while start < total:
        end = start + 1
        row = checks[start][0]
        while end < total and checks[end][0] == row:
            end += 1

        for i in range(start, end):
            _, kind, left, right = checks[i]
            if kind == 0:
                k = left
                while k <= m:
                    bit[k] += 1
                    k += k & -k
                if right != left:
                    k = right
                    while k <= m:
                        bit[k] += 1
                        k += k & -k

        for i in range(start, end):
            _, _, left, right = checks[i]
            count = 0
            k = right
            while k:
                count += bit[k]
                k -= k & -k
            k = left - 1
            while k:
                count -= bit[k]
                k -= k & -k

            if count != (1 if left == right else 2):
                sys.stdout.write("syntax error\n")
                return

        for i in range(start, end):
            _, kind, left, right = checks[i]
            if kind == 1:
                k = left
                while k <= m:
                    bit[k] -= 1
                    k += k & -k
                if right != left:
                    k = right
                    while k <= m:
                        bit[k] -= 1
                        k += k & -k

        start = end

    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
