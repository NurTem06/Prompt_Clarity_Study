import sys

def main():
    a, b, x = map(int, sys.stdin.buffer.read().split())
    runs = x + 1

    start = 0
    if a < (runs + 1) // 2 or b < runs // 2:
        start = 1

    zero_runs = (runs + (1 if start == 0 else 0)) // 2
    one_runs = runs - zero_runs
    extra = [a - zero_runs, b - one_runs]

    result = []
    for i in range(runs):
        digit = (start + i) % 2
        result.append(str(digit) * (1 + extra[digit]))
        extra[digit] = 0

    print("".join(result))

if __name__ == "__main__":
    main()