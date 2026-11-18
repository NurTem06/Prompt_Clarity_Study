import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data
    if k > n * n:
        print(-1)
        return

    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        if k:
            matrix[i][i] = 1
            k -= 1
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = matrix[j][i] = 1
                k -= 2

    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in matrix))

if __name__ == "__main__":
    main()
