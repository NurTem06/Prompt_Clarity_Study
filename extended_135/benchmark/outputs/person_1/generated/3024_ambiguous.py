import sys
import random


def main():
    s = sys.stdin.buffer.read().strip()
    n = len(s)
    mod = 1_000_000_007
    base = random.randrange(256, mod - 1)

    left_hash = right_hash = 0
    power = 1
    boundary = 0
    answer = 0

    for i in range(n // 2):
        j = n - 1 - i
        left_hash = (left_hash * base + s[i]) % mod
        right_hash = (s[j] * power + right_hash) % mod

        if left_hash == right_hash and s[boundary:i + 1] == s[j:n - boundary]:
            answer += 2
            boundary = i + 1
            left_hash = right_hash = 0
            power = 1
        else:
            power = power * base % mod

    if boundary * 2 < n:
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
