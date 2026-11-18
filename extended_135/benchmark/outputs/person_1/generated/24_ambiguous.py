import sys

def main():
    board = [line.strip().decode() for line in sys.stdin.buffer.read().split()]
    directions = ((0, 1), (1, 0), (1, 1), (1, -1))

    for r in range(10):
        for c in range(10):
            if board[r][c] != '.':
                continue
            for dr, dc in directions:
                count = 1
                for sign in (-1, 1):
                    nr, nc = r + sign * dr, c + sign * dc
                    while 0 <= nr < 10 and 0 <= nc < 10 and board[nr][nc] == 'X':
                        count += 1
                        nr += sign * dr
                        nc += sign * dc
                if count >= 5:
                    print("YES")
                    return
    print("NO")

if __name__ == "__main__":
    main()