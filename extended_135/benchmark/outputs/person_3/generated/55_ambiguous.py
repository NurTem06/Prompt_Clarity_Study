import sys


def main():
    n, k = map(int, sys.stdin.buffer.read().split())

    counts = {}
    for exponent in range(n.bit_length()):
        if (n >> exponent) & 1:
            counts[exponent] = 1

    total = len(counts)
    if total > k:
        sys.stdout.write("No\n")
        return

    highest = n.bit_length() - 1

    while total + counts[highest] <= k:
        amount = counts.pop(highest)
        counts[highest - 1] = counts.get(highest - 1, 0) + 2 * amount
        total += amount
        highest -= 1

    answer = []
    for exponent in sorted(counts, reverse=True):
        answer.extend([exponent] * counts[exponent])

    for _ in range(k - total):
        exponent = answer.pop() - 1
        answer.append(exponent)
        answer.append(exponent)

    sys.stdout.write("Yes\n" + " ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()