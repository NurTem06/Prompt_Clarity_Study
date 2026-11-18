import sys

n = int(sys.stdin.buffer.readline())
place = 10 ** (len(str(n)) - 1)
print((n // place + 1) * place - n)