import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]

    prefix = [0]
    current = 0
    minimum = 0
    maximum = 0
    seen = {0}

    for difference in data[1:]:
        current += difference
        if current in seen:
            print(-1)
            return
        seen.add(current)
        prefix.append(current)
        minimum = min(minimum, current)
        maximum = max(maximum, current)

    if maximum - minimum != n - 1:
        print(-1)
        return

    shift = 1 - minimum
    sys.stdout.write(" ".join(str(value + shift) for value in prefix))


if __name__ == "__main__":
    main()
