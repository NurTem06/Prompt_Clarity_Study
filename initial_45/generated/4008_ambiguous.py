import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    groups = {}
    for i, value in enumerate(data[2:2 + n]):
        groups.setdefault(value, []).append(i)

    if any(len(indices) > k for indices in groups.values()):
        sys.stdout.write("NO\n")
        return

    colors = [0] * n
    current = 0
    for indices in groups.values():
        for i in indices:
            colors[i] = current + 1
            current = (current + 1) % k

    sys.stdout.write("YES\n" + " ".join(map(str, colors)) + "\n")


if __name__ == "__main__":
    main()
