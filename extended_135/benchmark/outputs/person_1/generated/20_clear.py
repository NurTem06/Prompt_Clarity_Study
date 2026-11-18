import sys

h, m = map(int, sys.stdin.readline().strip().split(':'))
current = h * 60 + m

for delay in range(1440):
    time = (current + delay) % 1440
    hour, minute = divmod(time, 60)
    if hour // 10 == minute % 10 and hour % 10 == minute // 10:
        print(delay)
        break