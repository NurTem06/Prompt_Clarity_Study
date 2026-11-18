import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    swaps = data[n + 1]
    prefix_max = 0

    for i in range(n - 1):
        prefix_max = max(prefix_max, int(data[i + 1]))
        if swaps[i] == 48 and prefix_max != i + 1:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
