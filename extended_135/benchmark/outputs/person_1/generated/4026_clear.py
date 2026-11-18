import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 1
    answers = []

    for _ in range(data[0]):
        n, m = data[pos], data[pos + 1]
        pos += 2
        symmetric = False

        for _ in range(n):
            if data[pos + 1] == data[pos + 2]:
                symmetric = True
            pos += 4

        answers.append("YES" if m % 2 == 0 and symmetric else "NO")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
