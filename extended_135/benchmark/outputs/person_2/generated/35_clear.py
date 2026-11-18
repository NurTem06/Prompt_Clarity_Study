import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = map(int, data[:2])
    grid = data[2:2 + n]

    if n % 3 == 0:
        h = n // 3
        colors = [grid[i * h][0] for i in range(3)]
        if len(set(colors)) == 3 and all(
            grid[r] == bytes([colors[r // h]]) * m for r in range(n)
        ):
            print("YES")
            return

    if m % 3 == 0:
        w = m // 3
        colors = [grid[0][i * w] for i in range(3)]
        if len(set(colors)) == 3:
            expected = b"".join(bytes([color]) * w for color in colors)
            if all(row == expected for row in grid):
                print("YES")
                return

    print("NO")


if __name__ == "__main__":
    main()
