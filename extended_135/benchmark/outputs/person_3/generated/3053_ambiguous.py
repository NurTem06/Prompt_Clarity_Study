import sys
from itertools import product


def main():
    N, K, P = map(int, sys.stdin.buffer.readline().split())

    if K > N - P // 2:
        print("IMPOSSIBLE")
        return

    if K == 1:
        print("a" * N if P == N else "IMPOSSIBLE")
        return

    if K == 2:
        if P <= 3:
            if N > 8:
                print("IMPOSSIBLE")
                return

            for chars in product("ab", repeat=N):
                s = "".join(chars)
                if "a" not in s or "b" not in s:
                    continue
                if any(
                    s[i:i + length] == s[i:i + length][::-1]
                    for length in (P + 1, P + 2)
                    for i in range(N - length + 1)
                ):
                    continue
                if any(
                    s[i:i + P] == s[i:i + P][::-1]
                    for i in range(N - P + 1)
                ):
                    print(s)
                    return

            print("IMPOSSIBLE")
            return

        if N == P:
            if P % 2:
                side = "a" * (P // 2)
                print(side + "b" + side)
            else:
                side = "a" * (P // 2 - 1)
                print(side + "bb" + side)
        else:
            remaining = N - P
            print("a" * P + ("babbaa" * ((remaining + 5) // 6))[:remaining])
        return

    alphabet = b"abcdefghijklmnopqrstuvwxyz"[:K]
    half_length = (P + 1) // 2
    half = (alphabet * ((half_length + K - 1) // K))[:half_length]

    result = bytearray(half)
    if P % 2:
        result.extend(half[:-1][::-1])
    else:
        result.extend(half[::-1])

    if half_length < K:
        result.extend(alphabet[half_length:])

    while len(result) < N:
        last = result[-1]
        previous = result[-2] if len(result) > 1 else -1
        if last != 97 and previous != 97:
            result.append(97)
        elif last != 98 and previous != 98:
            result.append(98)
        else:
            result.append(99)

    sys.stdout.buffer.write(result)
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()