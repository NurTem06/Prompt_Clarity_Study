import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, d = data[:3]
    lengths = data[3:3 + m]
    water = n - sum(lengths)

    if water > (m + 1) * (d - 1):
        print("NO")
        return

    answer = []
    for i, length in enumerate(lengths, 1):
        gap = min(water, d - 1)
        answer.extend([0] * gap)
        answer.extend([i] * length)
        water -= gap

    answer.extend([0] * water)
    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()