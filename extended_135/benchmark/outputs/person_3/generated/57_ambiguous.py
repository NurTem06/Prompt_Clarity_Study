import sys

data = list(map(int, sys.stdin.buffer.read().split()))
xs = data[1::2]
ys = data[2::2]

width = max(xs) - min(xs)
height = max(ys) - min(ys)

print(width * height if width and height else -1)