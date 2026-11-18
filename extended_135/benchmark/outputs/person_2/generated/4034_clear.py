import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    s = data[1]
    tails = [-1, -1]
    colors = []

    for ch in s:
        choice = -1
        for color in range(2):
            if tails[color] <= ch:
                if choice == -1 or tails[color] > tails[choice]:
                    choice = color

        if choice == -1:
            print("NO")
            return

        tails[choice] = ch
        colors.append(str(choice))

    print("YES")
    print("".join(colors))


if __name__ == "__main__":
    main()