import sys
from collections import Counter


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:n + 1]
    total = sum(a)
    counts = Counter(a)
    answer = []

    for i, value in enumerate(a, 1):
        remaining_sum = total - value
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            if counts.get(target, 0) > (target == value):
                answer.append(str(i))

    sys.stdout.write(str(len(answer)) + "\n" + " ".join(answer) + "\n")


if __name__ == "__main__":
    main()