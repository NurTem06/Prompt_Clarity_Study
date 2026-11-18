import sys

n, a, b = map(int, sys.stdin.buffer.read().split())
answer = 0

for first_plates in range(1, n):
    second_plates = n - first_plates
    answer = max(answer, min(a // first_plates, b // second_plates))

print(answer)
