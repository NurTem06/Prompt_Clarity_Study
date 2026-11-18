import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(data)
    answers = []

    for _ in range(t):
        n = next(data)
        prev_p = prev_c = 0
        valid = True

        for _ in range(n):
            p = next(data)
            c = next(data)
            if p < prev_p or c < prev_c or c - prev_c > p - prev_p:
                valid = False
            prev_p, prev_c = p, c

        answers.append("YES" if valid else "NO")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()