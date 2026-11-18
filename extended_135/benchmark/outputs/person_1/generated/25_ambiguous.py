import sys

def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    if k > n * n:
        print(-1)
        return

    matrix = [[0] * n for _ in range(n)]
    diagonals = n
    pairs = n * (n - 1) // 2

    for i in range(n):
        for j in range(i, n):
            if i == j:
                diagonals -= 1
                cost = 1
            else:
                pairs -= 1
                cost = 2

            remaining = k - cost
            if (0 <= remaining <= diagonals + 2 * pairs
                    and (diagonals > 0 or remaining % 2 == 0)):
                matrix[i][j] = matrix[j][i] = 1
                k = remaining

    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in matrix))

if __name__ == "__main__":
    main()