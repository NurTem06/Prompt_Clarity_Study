import sys


def main():
    data = sys.stdin.buffer.read().split()
    text, pattern = data[0], data[1]
    n, m = len(text), len(pattern)

    if m > n:
        print(0)
        return

    previous = [-1] * 26
    distances = [0] * m
    for i, c in enumerate(pattern):
        c -= 97
        if previous[c] != -1:
            distances[i] = i - previous[c]
        previous[c] = i

    failure = [0] * m
    j = 0
    for i in range(1, m):
        d = distances[i]
        while j and distances[j] != d and (distances[j] != 0 or d <= j):
            j = failure[j - 1]
        j += 1
        failure[i] = j

    previous = [-1] * 26
    j = 0
    count = 0
    match_start = 0

    for i, c in enumerate(text):
        c -= 97
        last = previous[c]
        d = 0 if last == -1 else i - last
        previous[c] = i

        while j and distances[j] != d and (distances[j] != 0 or d <= j):
            j = failure[j - 1]
        j += 1

        if j == m:
            count += 1
            match_start = i - m + 1
            j = failure[j - 1]

    if count == 1:
        sys.stdout.buffer.write(text[match_start:match_start + m] + b"\n")
    else:
        print(count)


if __name__ == "__main__":
    main()
