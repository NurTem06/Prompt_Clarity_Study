import sys
from collections import Counter


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    counts = Counter(data[1:])
    matrix = [[0] * n for _ in range(n)]
    half = n // 2

    if n % 2:
        odd = [value for value, count in counts.items() if count % 2]
        if len(odd) != 1:
            print("NO")
            return
        center = odd[0]
        matrix[half][half] = center
        counts[center] -= 1
    elif any(count % 4 for count in counts.values()):
        print("NO")
        return

    keys = list(counts)
    index = 0

    for i in range(half):
        for j in range(half):
            while index < len(keys) and counts[keys[index]] < 4:
                index += 1
            if index == len(keys):
                print("NO")
                return

            value = keys[index]
            counts[value] -= 4
            matrix[i][j] = value
            matrix[i][n - 1 - j] = value
            matrix[n - 1 - i][j] = value
            matrix[n - 1 - i][n - 1 - j] = value

    if n % 2:
        pairs = []
        for value, count in counts.items():
            pairs.extend([value] * (count // 2))

        if len(pairs) != 2 * half:
            print("NO")
            return

        for i in range(half):
            value = pairs.pop()
            matrix[i][half] = matrix[n - 1 - i][half] = value

        for j in range(half):
            value = pairs.pop()
            matrix[half][j] = matrix[half][n - 1 - j] = value

    print("YES")
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in matrix))


if __name__ == "__main__":
    main()
