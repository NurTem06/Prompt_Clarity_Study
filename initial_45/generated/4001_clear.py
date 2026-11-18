import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    divisors = Counter(data[1:])
    x = max(divisors)

    for d in list(divisors):
        if x % d == 0:
            divisors[d] -= 1
            if divisors[d] == 0:
                del divisors[d]

    y = max(divisors)
    print(x, y)

if __name__ == "__main__":
    main()