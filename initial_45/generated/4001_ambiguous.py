import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    counts = Counter(data[1:1 + data[0]])
    x = max(counts)
    for d in range(1, x + 1):
        if x % d == 0:
            counts[d] -= 1
    y = max(d for d, count in counts.items() if count > 0)
    print(x, y)

if __name__ == "__main__":
    main()