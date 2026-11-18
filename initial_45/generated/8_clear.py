import sys
from collections import Counter

def main():
    tiles = sys.stdin.read().split()
    counts = Counter(tiles)
    answer = 2

    for suit in "mps":
        for number in range(1, 10):
            answer = min(answer, 3 - counts[f"{number}{suit}"])
        for start in range(1, 8):
            present = sum(counts[f"{number}{suit}"] > 0
                          for number in range(start, start + 3))
            answer = min(answer, 3 - present)

    print(answer)

if __name__ == "__main__":
    main()