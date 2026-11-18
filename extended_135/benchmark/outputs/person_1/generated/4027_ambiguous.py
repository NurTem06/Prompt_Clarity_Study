import sys

n = int(sys.stdin.buffer.read())
print((n * (n + 1) // 2) % 2)