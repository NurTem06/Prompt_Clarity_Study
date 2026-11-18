import sys


def main():
    s = sys.stdin.buffer.readline().strip()
    n = len(s)

    sa = list(range(n))
    rank = list(s)
    step = 1
    base = 257

    while True:
        limit = n - step
        keys = [
            (rank[i] + 1) * base + (rank[i + step] + 1 if i < limit else 0)
            for i in range(n)
        ]
        sa.sort(key=keys.__getitem__)

        new_rank = [0] * n
        classes = 1
        previous = keys[sa[0]]

        for j in range(1, n):
            index = sa[j]
            current = keys[index]
            if current != previous:
                classes += 1
                previous = current
            new_rank[index] = classes - 1

        rank = new_rank
        if classes == n:
            break

        base = classes + 1
        step <<= 1

    del keys, new_rank

    best_length = 0
    best_rank = n
    best_start = 0
    length = 0

    for i in range(n):
        position = rank[i]
        if position == 0:
            length = 0
            continue

        j = sa[position - 1]
        while i + length < n and j + length < n and s[i + length] == s[j + length]:
            length += 1

        if length > best_length or (length == best_length and position < best_rank):
            best_length = length
            best_rank = position
            best_start = i

        if length:
            length -= 1

    sys.stdout.buffer.write(s[best_start:best_start + best_length] + b"\n")


if __name__ == "__main__":
    main()