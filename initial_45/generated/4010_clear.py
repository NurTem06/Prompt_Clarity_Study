import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    answers = []

    for _ in range(t):
        n = data[pos]
        pos += 1
        first = [-1] * (n + 1)
        found = False

        for i in range(n):
            value = data[pos + i]
            if first[value] == -1:
                first[value] = i
            elif i - first[value] >= 2:
                found = True

        pos += n
        answers.append("YES" if found else "NO")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()