import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    m = data[1]
    ascending = []
    descending = []

    for i in range(m):
        u = data[2 + 2 * i]
        v = data[3 + 2 * i]
        if u < v:
            ascending.append(i + 1)
        else:
            descending.append(i + 1)

    removed = ascending if len(ascending) <= len(descending) else descending
    sys.stdout.write(str(len(removed)) + "\n")
    if removed:
        sys.stdout.write("\n".join(map(str, removed)) + "\n")


if __name__ == "__main__":
    main()