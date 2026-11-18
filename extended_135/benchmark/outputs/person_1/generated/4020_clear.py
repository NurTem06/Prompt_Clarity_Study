import sys

times = sys.stdin.read().split()
h1, m1 = map(int, times[0].split(':'))
h2, m2 = map(int, times[1].split(':'))

midpoint = (h1 * 60 + m1 + h2 * 60 + m2) // 2
hour, minute = divmod(midpoint, 60)
print(f"{hour:02d}:{minute:02d}")