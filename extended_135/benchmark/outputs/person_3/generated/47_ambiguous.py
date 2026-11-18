import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x = data[0], data[1]

    before = during = after = answer = 0

    for i in range(2, n + 2):
        value = data[i]
        multiplied = value * x

        after = max(0, after + value, during + value)
        during = max(0, during + multiplied, before + multiplied)
        before = max(0, before + value)

        answer = max(answer, before, during, after)

    print(answer)


if __name__ == "__main__":
    main()