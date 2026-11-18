import sys


def main():
    text = sys.stdin.buffer.readline().strip()
    pattern = sys.stdin.buffer.readline().strip()
    n, m = len(text), len(pattern)

    if m > n:
        print(0)
        return

    if m == 1:
        if n == 1:
            sys.stdout.buffer.write(text + b"\n")
        else:
            print(n)
        return

    previous = [0] * m
    last = [-1] * 26

    for i, c in enumerate(pattern):
        c -= 97
        if last[c] != -1:
            previous[i] = i - last[c]
        last[c] = i

    prefix = [0] * m
    j = 0

    for i in range(1, m):
        distance = previous[i]
        while True:
            expected = previous[j]
            if distance == expected or (expected == 0 and distance > j):
                j += 1
                break
            if j == 0:
                break
            j = prefix[j - 1]
        prefix[i] = j

    last = [-1] * 26
    j = 0
    count = 0
    start = 0

    for i, c in enumerate(text):
        c -= 97
        distance = 0 if last[c] == -1 else i - last[c]
        last[c] = i

        while True:
            expected = previous[j]
            if distance == expected or (expected == 0 and distance > j):
                j += 1
                break
            if j == 0:
                break
            j = prefix[j - 1]

        if j == m:
            count += 1
            start = i - m + 1
            j = prefix[j - 1]

    if count == 1:
        sys.stdout.buffer.write(text[start:start + m] + b"\n")
    else:
        print(count)


if __name__ == "__main__":
    main()
