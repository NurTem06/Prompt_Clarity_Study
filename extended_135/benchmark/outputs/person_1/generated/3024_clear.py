import sys
import random


def main():
    s = sys.stdin.buffer.read().strip()
    n = len(s)

    base = random.randrange(256, 1 << 30) | 1
    mask = (1 << 64) - 1

    left = 0
    right = n - 1
    chunk_start = 0
    chunk_end = n

    left_hash = 0
    right_hash = 0
    power = 1
    answer = 0

    while left < right:
        left_hash = (left_hash * base + s[left]) & mask
        right_hash = (right_hash + s[right] * power) & mask

        if (left_hash == right_hash
                and s[chunk_start:left + 1] == s[right:chunk_end]):
            answer += 2
            chunk_start = left + 1
            chunk_end = right
            left_hash = 0
            right_hash = 0
            power = 1
        else:
            power = (power * base) & mask

        left += 1
        right -= 1

    if chunk_start < chunk_end:
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
