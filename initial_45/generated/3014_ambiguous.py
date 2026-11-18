import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    forward = []
    backward = []

    for i in range(m):
        u = data[2 + 2 * i]
        v = data[3 + 2 * i]
        if u < v:
            forward.append(i + 1)
        else:
            backward.append(i + 1)

    removed = forward if len(forward) <= len(backward) else backward
    sys.stdout.write("\n".join(map(str, [len(removed)] + removed)) + "\n")


if __name__ == "__main__":
    main()
