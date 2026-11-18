import sys

def main():
    a, b = sys.stdin.read().split()

    if len(a) < len(b):
        print(''.join(sorted(a, reverse=True)))
        return

    counts = [0] * 10
    for digit in a:
        counts[int(digit)] += 1

    n = len(a)

    def search(pos):
        if pos == n:
            return ""

        limit = int(b[pos])
        for digit in range(limit, -1, -1):
            if counts[digit] == 0 or (pos == 0 and digit == 0):
                continue

            counts[digit] -= 1

            if digit < limit:
                suffix = ''.join(
                    str(d) * counts[d] for d in range(9, -1, -1)
                )
                return str(digit) + suffix

            suffix = search(pos + 1)
            if suffix is not None:
                return str(digit) + suffix

            counts[digit] += 1

        return None

    print(search(0))

if __name__ == "__main__":
    main()