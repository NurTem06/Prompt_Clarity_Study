import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    starts = [0] * m
    deadlines = [0] * m
    remaining = [0] * m
    exam_on = [-1] * (n + 1)

    pos = 2
    for i in range(m):
        s, d, c = data[pos:pos + 3]
        pos += 3
        starts[i] = s
        deadlines[i] = d
        remaining[i] = c
        exam_on[d] = i

    schedule = [0] * n

    for day in range(1, n + 1):
        exam = exam_on[day]
        if exam != -1:
            if remaining[exam]:
                print(-1)
                return
            schedule[day - 1] = m + 1
            continue

        best = -1
        for i in range(m):
            if remaining[i] and starts[i] <= day < deadlines[i]:
                if best == -1 or deadlines[i] < deadlines[best]:
                    best = i

        if best != -1:
            schedule[day - 1] = best + 1
            remaining[best] -= 1

    print(*schedule)


if __name__ == "__main__":
    main()