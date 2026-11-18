import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, r = data[:2]
    a = data[2:]

    nearest = [-1] * n
    last = -1
    for i in range(n):
        if a[i]:
            last = i
        nearest[i] = last

    position = 0
    answer = 0
    while position < n:
        heater = nearest[min(n - 1, position + r - 1)]
        if heater < max(0, position - r + 1):
            print(-1)
            return
        answer += 1
        position = heater + r

    print(answer)


if __name__ == "__main__":
    main()
