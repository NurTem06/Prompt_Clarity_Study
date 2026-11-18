import sys

def main():
    s = sys.stdin.buffer.readline().strip().decode()
    length = len(s)
    best = float("inf")

    for ending in ("00", "25", "50", "75"):
        for i in range(length):
            if s[i] != ending[0]:
                continue
            for j in range(length):
                if i == j or s[j] != ending[1]:
                    continue

                moves = (length - 1 - j) + (length - 2 - i + (i > j))
                remaining = [s[k] for k in range(length) if k != i and k != j]

                if remaining:
                    first_nonzero = next(
                        (k for k, digit in enumerate(remaining) if digit != "0"),
                        None
                    )
                    if first_nonzero is None:
                        continue
                    moves += first_nonzero
                elif ending[0] == "0":
                    continue

                best = min(best, moves)

    print(-1 if best == float("inf") else best)

if __name__ == "__main__":
    main()
