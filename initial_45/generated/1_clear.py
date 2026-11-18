import sys

def main():
    s = sys.stdin.buffer.read().strip().decode()
    best = int(s)
    best_sum = sum(map(int, s))

    for i, ch in enumerate(s):
        if ch == '0':
            continue
        candidate_s = s[:i] + str(int(ch) - 1) + '9' * (len(s) - i - 1)
        candidate = int(candidate_s)
        digit_sum = sum(map(int, candidate_s))
        if digit_sum > best_sum or (digit_sum == best_sum and candidate > best):
            best = candidate
            best_sum = digit_sum

    print(best)

if __name__ == "__main__":
    main()