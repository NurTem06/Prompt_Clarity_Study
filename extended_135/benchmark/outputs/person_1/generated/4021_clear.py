import sys

a = int(sys.stdin.buffer.read())
print((a - 1).bit_length())