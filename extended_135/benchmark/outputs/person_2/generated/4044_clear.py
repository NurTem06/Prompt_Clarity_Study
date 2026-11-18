import sys

def main():
    a, b, x = map(int, sys.stdin.buffer.read().split())
    runs = x + 1

    for start in (0, 1):
        zero_runs = (runs + 1) // 2 if start == 0 else runs // 2
        one_runs = runs - zero_runs
        if zero_runs > a or one_runs > b:
            continue

        extra = [a - zero_runs, b - one_runs]
        result = []
        for i in range(runs):
            digit = (start + i) % 2
            result.append(str(digit) * (1 + extra[digit]))
            extra[digit] = 0

        print(''.join(result))
        return

if __name__ == "__main__":
    main()