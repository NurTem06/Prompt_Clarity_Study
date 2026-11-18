import sys


def main():
    s = sys.stdin.buffer.readline().strip()
    n = len(s)
    sa = list(range(n))
    rank = [c - 96 for c in s]
    base = max(n + 1, 27)
    step = 1

    while step < n:
        limit = n - step
        keys = [
            rank[i] * base + (rank[i + step] if i < limit else 0)
            for i in range(n)
        ]
        sa.sort(key=keys.__getitem__)

        new_rank = [0] * n
        classes = 0
        previous = -1
        for i in sa:
            key = keys[i]
            if key != previous:
                classes += 1
                previous = key
            new_rank[i] = classes

        rank = new_rank
        if classes == n:
            break
        step <<= 1

    best_length = 0
    best_rank = n + 1
    best_start = 0
    common = 0

    for i in range(n):
        r = rank[i] - 1
        if r == 0:
            common = 0
            continue

        j = sa[r - 1]
        while i + common < n and j + common < n and s[i + common] == s[j + common]:
            common += 1

        if common > best_length or (common == best_length and r < best_rank):
            best_length = common
            best_rank = r
            best_start = i

        if common:
            common -= 1

    sys.stdout.buffer.write(s[best_start:best_start + best_length] + b"\n")


if __name__ == "__main__":
    main()