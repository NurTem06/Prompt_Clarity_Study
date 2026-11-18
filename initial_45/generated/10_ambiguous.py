import sys

n = int(sys.stdin.buffer.readline())
weeks, remainder = divmod(n, 7)
minimum = weeks * 2 + max(0, remainder - 5)
maximum = weeks * 2 + min(2, remainder)
print(minimum, maximum)