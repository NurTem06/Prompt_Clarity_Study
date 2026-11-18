import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
odd = sum(x % 2 for x in data[1:n + 1])
print(min(odd, n - odd))