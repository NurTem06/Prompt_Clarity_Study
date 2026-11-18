import sys


def main():
    a, b, c = map(int, sys.stdin.buffer.read().split())
    weeks = min(a // 3, b // 2, c // 2)
    remaining = [a - 3 * weeks, b - 2 * weeks, c - 2 * weeks]
    schedule = [0, 1, 2, 0, 2, 1, 0]

    best = 0
    for start in range(7):
        food = remaining[:]
        days = 0
        while True:
            kind = schedule[(start + days) % 7]
            if food[kind] == 0:
                break
            food[kind] -= 1
            days += 1
        best = max(best, days)

    print(weeks * 7 + best)


if __name__ == "__main__":
    main()
