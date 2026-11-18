import sys

s = sys.stdin.buffer.read().strip().decode()
best = int(s)
best_sum = sum(map(int, s))

for i, ch in enumerate(s):
    if ch == '0':
        continue
    candidate = s[:i] + str(int(ch) - 1) + '9' * (len(s) - i - 1)
    value = int(candidate)
    digit_sum = sum(map(int, candidate))
    if digit_sum > best_sum or (digit_sum == best_sum and value > best):
        best = value
        best_sum = digit_sum

print(best)
