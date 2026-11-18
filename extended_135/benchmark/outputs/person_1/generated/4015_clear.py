import sys

def main():
    n, m = map(int, sys.stdin.buffer.read().split())
    if m % n:
        print(-1)
        return

    ratio = m // n
    moves = 0
    for factor in (2, 3):
        while ratio % factor == 0:
            ratio //= factor
            moves += 1

    print(moves if ratio == 1 else -1)

if __name__ == "__main__":
    main()