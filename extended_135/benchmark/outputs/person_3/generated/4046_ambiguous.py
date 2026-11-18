import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]

    prefix = [0] * n
    minimum = maximum = 0

    for i in range(1, n):
        value = prefix[i - 1] + data[i]
        prefix[i] = value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    if maximum - minimum != n - 1:
        print(-1)
        return

    seen = bytearray(n)
    for value in prefix:
        index = value - minimum
        if seen[index]:
            print(-1)
            return
        seen[index] = 1

    shift = 1 - minimum
    sys.stdout.write(" ".join(str(value + shift) for value in prefix))


if __name__ == "__main__":
    main()
