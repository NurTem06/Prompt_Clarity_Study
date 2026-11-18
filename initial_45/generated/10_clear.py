import sys

n = int(sys.stdin.buffer.read())
weeks, days = divmod(n, 7)
print(weeks * 2 + max(0, days - 5), weeks * 2 + min(2, days))