import sys
from itertools import product


def main():
    n, k, p = map(int, sys.stdin.buffer.readline().split())

    if k > n - p // 2:
        print("IMPOSSIBLE")
        return

    if k == 1:
        print("a" * n if p == n else "IMPOSSIBLE")
        return

    if k == 2:
        if p >= 4:
            if n == p:
                print("a" + "b" * (p - 2) + "a")
            else:
                remaining = n - p
                tail = ("bbabaa" * ((remaining + 5) // 6))[:remaining]
                print("a" * p + tail)
            return

        if n > 8:
            print("IMPOSSIBLE")
            return

        for chars in product("ab", repeat=n):
            s = "".join(chars)
            if "a" not in s or "b" not in s:
                continue
            valid = True
            for length in (p + 1, p + 2):
                for start in range(n - length + 1):
                    part = s[start:start + length]
                    if part == part[::-1]:
                        valid = False
                        break
                if not valid:
                    break
            if valid and any(
                s[i:i + p] == s[i:i + p][::-1]
                for i in range(n - p + 1)
            ):
                print(s)
                return

        print("IMPOSSIBLE")
        return

    alphabet = "abcdefghijklmnopqrstuvwxyz"[:k]
    used = max(1, k - (n - p))
    arm = alphabet[1:used]
    palindrome = arm + "a" * (p - 2 * len(arm)) + arm[::-1]

    remaining = n - p
    cycle = alphabet[used:] + alphabet[:used]
    tail = (cycle * ((remaining + k - 1) // k))[:remaining]
    sys.stdout.write(palindrome + tail + "\n")


if __name__ == "__main__":
    main()
