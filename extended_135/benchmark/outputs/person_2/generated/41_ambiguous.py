import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    distances = [n] * n

    last = -n
    for i in range(n):
        if data[i + 1] == 0:
            last = i
        distances[i] = i - last

    last = 2 * n
    for i in range(n - 1, -1, -1):
        if data[i + 1] == 0:
            last = i
        distance = last - i
        if distance < distances[i]:
            distances[i] = distance

    sys.stdout.write(" ".join(map(str, distances)))


if __name__ == "__main__":
    main()