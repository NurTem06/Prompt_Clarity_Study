import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    distances = [0] * n

    last_zero = -n
    for i in range(n):
        if data[i + 1] == 0:
            last_zero = i
        distances[i] = i - last_zero

    next_zero = 2 * n
    for i in range(n - 1, -1, -1):
        if data[i + 1] == 0:
            next_zero = i
        distance = next_zero - i
        if distance < distances[i]:
            distances[i] = distance

    sys.stdout.write(" ".join(map(str, distances)))


if __name__ == "__main__":
    main()