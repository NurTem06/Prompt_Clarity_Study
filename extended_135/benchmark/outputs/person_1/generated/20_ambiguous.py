import sys

h, m = map(int, sys.stdin.readline().strip().split(':'))
start = h * 60 + m

for wait in range(1440):
    current = (start + wait) % 1440
    hour, minute = divmod(current, 60)
    if hour // 10 == minute % 10 and hour % 10 == minute // 10:
        print(wait)
        break