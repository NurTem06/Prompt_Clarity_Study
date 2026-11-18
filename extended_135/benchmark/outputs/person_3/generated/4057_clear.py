import sys
from collections import Counter

data = list(map(int, sys.stdin.buffer.read().split()))
print(max(Counter(data[1:1 + data[0]]).values()))