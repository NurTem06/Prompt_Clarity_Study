import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    counts = Counter(data[1:n + 1])
    print(max(counts.values()))

if __name__ == "__main__":
    main()