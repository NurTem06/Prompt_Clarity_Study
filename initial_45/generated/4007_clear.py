import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    f = data[1:n + 1]

    used = bytearray(n + 1)
    empty = []
    for i, value in enumerate(f):
        if value:
            used[value] = 1
        else:
            empty.append(i)

    missing = [value for value in range(1, n + 1) if not used[value]]
    bad = []

    for i, value in zip(empty, missing):
        f[i] = value
        if value == i + 1:
            bad.append(i)

    if len(bad) > 1:
        first = f[bad[0]]
        for j in range(len(bad) - 1):
            f[bad[j]] = f[bad[j + 1]]
        f[bad[-1]] = first
    elif bad:
        i = bad[0]
        j = empty[0] if empty[0] != i else empty[1]
        f[i], f[j] = f[j], f[i]

    sys.stdout.write(" ".join(map(str, f)))


if __name__ == "__main__":
    main()
