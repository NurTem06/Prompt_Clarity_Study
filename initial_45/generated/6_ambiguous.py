import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(data)
    answers = []

    for _ in range(t):
        n = next(data)
        x = next(data)
        max_damage = 0
        max_reduction = 0

        for _ in range(n):
            d = next(data)
            h = next(data)
            max_damage = max(max_damage, d)
            max_reduction = max(max_reduction, d - h)

        if x <= max_damage:
            answers.append("1")
        elif max_reduction == 0:
            answers.append("-1")
        else:
            remaining = x - max_damage
            answers.append(str((remaining + max_reduction - 1) // max_reduction + 1))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
