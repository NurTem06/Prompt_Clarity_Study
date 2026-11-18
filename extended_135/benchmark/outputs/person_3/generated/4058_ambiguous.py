import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, r = data[0], data[1]
    a = data[2:2 + n]

    nearest = [-1] * n
    last = -1
    for i, value in enumerate(a):
        if value == 1:
            last = i
        nearest[i] = last

    uncovered = 0
    answer = 0

    while uncovered < n:
        heater = nearest[min(n - 1, uncovered + r - 1)]
        if heater == -1 or heater < uncovered - r + 1:
            print(-1)
            return
        answer += 1
        uncovered = heater + r

    print(answer)


if __name__ == "__main__":
    main()