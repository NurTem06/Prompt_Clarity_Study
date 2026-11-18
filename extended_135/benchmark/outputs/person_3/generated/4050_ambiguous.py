import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:n + 1]
    groups = {}
    best = []

    for r in range(1, n + 1):
        total = 0
        for l in range(r, 0, -1):
            total += a[l - 1]
            blocks = groups.get(total)
            if blocks is None:
                blocks = [(l, r)]
                groups[total] = blocks
            elif l > blocks[-1][1]:
                blocks.append((l, r))

            if len(blocks) > len(best):
                best = blocks

    output = [str(len(best))]
    output.extend(f"{l} {r}" for l, r in best)
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
