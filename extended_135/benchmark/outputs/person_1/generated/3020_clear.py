import sys


def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return

    n = [int(ch) for ch in reversed(s)]
    length = len(n)

    if length % 2 == 0 or any(n[i] % 2 for i in range(1, length, 2)):
        print(-1)
        return

    size = (length + 1) // 2
    parity = [n[2 * i] % 2 for i in range(size)]
    first = next((i for i, digit in enumerate(n) if digit % 5), None)
    roots = []

    if first is None:
        roots.append([0] * size)
    elif first % 2 == 0:
        start = first // 2
        for leading in range(1, 5):
            if leading * leading % 5 != n[first] % 5:
                continue

            root = [0] * size
            root[start] = leading
            inverse = pow(2 * leading, -1, 5)

            for j in range(start + 1, size):
                k = start + j
                total = sum(
                    root[i] * root[k - i]
                    for i in range(start + 1, j)
                )
                root[j] = (n[k] - total) * inverse % 5

            roots.append(root)

    best = None
    for root in roots:
        digits = [
            value if value % 2 == parity[i] else value + 5
            for i, value in enumerate(root)
        ]

        square = [0] * length
        for i in range(size):
            for j in range(size):
                square[i + j] += digits[i] * digits[j]

        if any(square[i] % 10 != n[i] for i in range(length)):
            continue

        value = int("".join(map(str, reversed(digits))))
        if value > 0 and (best is None or value < best):
            best = value

    print(best if best is not None else -1)


if __name__ == "__main__":
    solve()
