import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, p = data[:3]
    board = data[3:]
    b = [[(-board[i * m + j]) % p for j in range(m)] for i in range(n)]

    size = n + m
    matrix = []

    for i in range(n):
        row = [0] * (size + 1)
        row[i] = (m - 1) % p
        for j in range(m):
            row[n + j] = 1
        row[size] = sum(b[i]) % p
        matrix.append(row)

    for j in range(m):
        row = [0] * (size + 1)
        for i in range(n):
            row[i] = 1
        row[n + j] = (n - 1) % p
        row[size] = sum(b[i][j] for i in range(n)) % p
        matrix.append(row)

    rank = 0
    pivots = []
    for col in range(size):
        pivot = next(
            (r for r in range(rank, size) if matrix[r][col]),
            None
        )
        if pivot is None:
            continue

        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        current = matrix[rank]
        inverse = pow(current[col], p - 2, p)
        for c in range(col, size + 1):
            current[c] = current[c] * inverse % p

        for r in range(rank + 1, size):
            other = matrix[r]
            factor = other[col]
            if factor:
                for c in range(col, size + 1):
                    other[c] = (other[c] - factor * current[c]) % p

        pivots.append(col)
        rank += 1

    for r in range(rank, size):
        if matrix[r][size]:
            print(-1)
            return

    solution = [0] * size
    for r in range(rank - 1, -1, -1):
        col = pivots[r]
        solution[col] = (
            matrix[r][size]
            - sum(matrix[r][c] * solution[c] for c in range(col + 1, size))
        ) % p

    moves = []
    for i in range(n):
        for j in range(m):
            count = (solution[i] + solution[n + j] - b[i][j]) % p
            moves.extend([str(i * m + j + 1)] * count)

    sys.stdout.write(str(len(moves)) + "\n")
    if moves:
        sys.stdout.write(" ".join(moves) + "\n")


if __name__ == "__main__":
    main()
