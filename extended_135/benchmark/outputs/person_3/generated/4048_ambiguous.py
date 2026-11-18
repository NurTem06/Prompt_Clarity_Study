import sys
from math import isqrt

def main():
    n = int(sys.stdin.buffer.readline())
    for a in range(isqrt(n), 0, -1):
        if n % a == 0:
            print(a + n // a - 2)
            return

if __name__ == "__main__":
    main()