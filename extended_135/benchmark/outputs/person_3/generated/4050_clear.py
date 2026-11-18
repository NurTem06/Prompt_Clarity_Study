import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:n + 1]
    blocks_by_sum = {}
    best = []

    for r in range(n):
        total = 0
        for l in range(r, -1, -1):
            total += a[l]
            blocks = blocks_by_sum.get(total)
            if blocks is None:
                blocks = [(l + 1, r + 1)]
                blocks_by_sum[total] = blocks
            elif blocks[-1][1] < l + 1:
                blocks.append((l + 1, r + 1))

            if len(blocks) > len(best):
                best = blocks

    output = [str(len(best))]
    output.extend(f"{l} {r}" for l, r in best)
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()