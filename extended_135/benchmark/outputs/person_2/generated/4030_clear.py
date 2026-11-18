import sys


def main():
    data = sys.stdin.buffer.read().split()
    s = data[1]
    best = [0] * 27
    colors = []

    for ch in s:
        x = ch - 97
        color = best[x + 1] + 1
        colors.append(str(color))
        while x >= 0 and best[x] < color:
            best[x] = color
            x -= 1

    sys.stdout.write(str(best[0]) + "\n" + " ".join(colors) + "\n")


if __name__ == "__main__":
    main()
