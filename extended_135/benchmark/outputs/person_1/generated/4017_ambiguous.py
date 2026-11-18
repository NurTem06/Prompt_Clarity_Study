import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:n + 1]

    total = 0
    largest = second_largest = 0

    for x in a:
        total += x
        if x >= largest:
            second_largest = largest
            largest = x
        elif x > second_largest:
            second_largest = x

    answer = []
    for i, x in enumerate(a, 1):
        remaining_max = second_largest if x == largest else largest
        if total - x == 2 * remaining_max:
            answer.append(str(i))

    sys.stdout.write(str(len(answer)) + "\n" + " ".join(answer) + "\n")


if __name__ == "__main__":
    main()