import sys
import math
from bisect import bisect_left, bisect_right
from functools import lru_cache


def main():
    B, N = map(int, sys.stdin.buffer.read().split())

    if N < B:
        print(N)
        return

    digits = [d for d in range(2, B) if N % d == 0]
    remaining = N
    for d in digits:
        while remaining % d == 0:
            remaining //= d
        if remaining == 1:
            break

    if remaining != 1:
        print("impossible")
        return

    largest = digits[-1]
    powers = [1]
    while powers[-1] < N:
        powers.append(powers[-1] * largest)

    min_length = len(powers) - 1

    limit = (1 << 63) - 1
    max_length = 0
    value = limit
    while value:
        max_length += 1
        value //= B

    max_length = min(max_length, N.bit_length() - 1)

    while len(powers) <= max_length:
        powers.append(powers[-1] * largest)

    @lru_cache(maxsize=30000)
    def pairs(n):
        lower = max(2, (n + largest - 1) // largest)
        upper = math.isqrt(n)
        left = bisect_left(digits, lower)
        right = bisect_right(digits, upper)
        return tuple(digits[i] for i in range(left, right)
                     if n % digits[i] == 0)

    @lru_cache(maxsize=200000)
    def search(n, count, minimum):
        if count == 1:
            if minimum <= n <= largest:
                return (n,)
            return None

        if n > powers[count] or minimum ** count > n:
            return None

        if count == 2:
            choices = pairs(n)
            index = bisect_left(choices, minimum)
            if index < len(choices):
                d = choices[index]
                return (d, n // d)
            return None

        lower = max(minimum, (n + powers[count - 1] - 1)
                    // powers[count - 1])

        upper = int(n ** (1.0 / count))
        while (upper + 1) ** count <= n:
            upper += 1
        while upper ** count > n:
            upper -= 1

        left = bisect_left(digits, lower)
        right = bisect_right(digits, upper)

        for i in range(left, right):
            d = digits[i]
            if n % d:
                continue
            tail = search(n // d, count - 1, d)
            if tail is not None:
                return (d,) + tail
        return None

    for length in range(min_length, max_length + 1):
        answer = search(N, length, 2)
        if answer is not None:
            result = 0
            for d in answer:
                result = result * B + d
            print(result)
            return

    print("impossible")


if __name__ == "__main__":
    main()
