import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, p = data[:3]
    board = data[3:]
    target = [[(-board[i * m + j]) % p for j in range(m)] for i in range(n)]

    size = n + m
    matrix = []

    for i in range(n):
        row = [0] * (size + 1)
        row[i] = (m - 1) % p
        for j in range(m):
            row[n + j] = 1
        row[size] = sum(target[i]) % p
        matrix.append(row)

    for j in range(m):
        row = [0] * (size + 1)
        for i in range(n):
            row[i] = 1
        row[n + j] = (n - 1) % p
        row[size] = sum(target[i][j] for i in range(n)) % p
        matrix.append(row)

    pivots = []
    rank = 0

    for col in range(size):
        pivot = next((r for r in range(rank, size) if matrix[r][col]), None)
        if pivot is None:
            continue

        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_row = matrix[rank]
        inv = pow(pivot_row[col], p - 2, p)
        for k in range(col, size + 1):
            pivot_row[k] = pivot_row[k] * inv % p

        for r in range(rank + 1, size):
            factor = matrix[r][col]
            if factor:
                row = matrix[r]
                for k in range(col, size + 1):
                    row[k] = (row[k] - factor * pivot_row[k]) % p

        pivots.append(col)
        rank += 1

    for r in range(rank, size):
        if matrix[r][size]:
            sys.stdout.write("-1\n")
            return

    solution = [0] * size
    for r in range(rank - 1, -1, -1):
        col = pivots[r]
        row = matrix[r]
        solution[col] = (
            row[size] - sum(row[k] * solution[k] for k in range(col + 1, size))
        ) % p

    moves = []
    for i in range(n):
        for j in range(m):
            count = (solution[i] + solution[n + j] - target[i][j]) % p
            moves.extend([str(i * m + j + 1)] * count)

    sys.stdout.write(str(len(moves)) + "\n")
    if moves:
        sys.stdout.write(" ".join(moves) + "\n")


if __name__ == "__main__":
    main()
