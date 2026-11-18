import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x = data[0], data[1]

    before = during = after = 0
    answer = 0

    for i in range(2, n + 2):
        value = data[i]
        after = max(after, during, 0) + value
        during = max(during, before, 0) + value * x
        before = max(before, 0) + value
        answer = max(answer, before, during, after)

    print(answer)


if __name__ == "__main__":
    main()
