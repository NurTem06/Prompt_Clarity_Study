import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    s = list(data[1])
    t = list(data[2])

    if sorted(s) != sorted(t):
        print(-1)
        return

    moves = []
    for i in range(n):
        j = i
        while s[j] != t[i]:
            j += 1
        while j > i:
            s[j - 1], s[j] = s[j], s[j - 1]
            moves.append(j)
            j -= 1

    print(len(moves))
    if moves:
        print(*moves)


if __name__ == "__main__":
    main()