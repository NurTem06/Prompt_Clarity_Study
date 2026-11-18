import sys


def main():
    s = sys.stdin.buffer.readline().strip().decode()
    length = len(s)
    if length < 2:
        print(-1)
        return

    answer = float("inf")

    for i in range(length):
        for j in range(length):
            if i == j or s[i] + s[j] not in ("00", "25", "50", "75"):
                continue

            prefix = [s[k] for k in range(length) if k != i and k != j]

            if prefix and prefix[0] == "0":
                first_nonzero = next(
                    (k for k, digit in enumerate(prefix) if digit != "0"), -1
                )
                if first_nonzero == -1:
                    continue
                prefix.insert(0, prefix.pop(first_nonzero))

            target = prefix + [s[i], s[j]]
            if target[0] == "0":
                continue

            current = list(s)
            moves = 0
            for k, digit in enumerate(target):
                position = current.index(digit, k)
                moves += position - k
                current.insert(k, current.pop(position))

            answer = min(answer, moves)

    print(-1 if answer == float("inf") else answer)


if __name__ == "__main__":
    main()