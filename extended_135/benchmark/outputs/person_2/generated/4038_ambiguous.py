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
        value = odd[0]
        matrix[half][half] = value
        counts[value] -= 1
    elif any(count % 4 for count in counts.values()):
        print("NO")
        return

    if sum(count // 4 for count in counts.values()) < half * half:
        print("NO")
        return

    keys = list(counts)
    index = 0
    for row in range(half):
        for col in range(half):
            while counts[keys[index]] < 4:
                index += 1
            value = keys[index]
            counts[value] -= 4
            matrix[row][col] = value
            matrix[row][n - 1 - col] = value
            matrix[n - 1 - row][col] = value
            matrix[n - 1 - row][n - 1 - col] = value

    if n % 2:
        pairs = []
        for value, count in counts.items():
            pairs.extend([value] * (count // 2))

        for i in range(half):
            value = pairs.pop()
            matrix[half][i] = matrix[half][n - 1 - i] = value

            value = pairs.pop()
            matrix[i][half] = matrix[n - 1 - i][half] = value

    output = ["YES"]
    output.extend(" ".join(map(str, row)) for row in matrix)
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
