import sys
from math import isqrt

def main():
    n = int(sys.stdin.buffer.readline())
    for d in range(isqrt(n), 0, -1):
        if n % d == 0:
            print(d + n // d - 2)
            return

if __name__ == "__main__":
    main()
