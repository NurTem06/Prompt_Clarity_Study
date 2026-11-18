import sys
from functools import lru_cache


def main():
    s = sys.stdin.buffer.read().strip().decode()
    if not s:
        return

    digits = tuple(map(int, s))
    falling = False

    for a, b in zip(digits, digits[1:]):
        if b < a:
            falling = True
        elif b > a and falling:
            print(-1)
            return

    length = len(digits)

    @lru_cache(maxsize=None)
    def count(pos, last, falling, tight):
        if pos == length:
            return 1

        limit = digits[pos] if tight else 9
        if falling:
            limit = min(limit, last)

        total = 0
        for digit in range(limit + 1):
            total += count(
                pos + 1,
                digit,
                falling or digit < last,
                tight and digit == digits[pos],
            )
        return total

    print(count(0, 0, False, True) - 1)


if __name__ == "__main__":
    main()