import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, length = data[:2]
    a = data[2:2 + n]
    b = set(data[2 + n:2 + 2 * n])

    for target in b:
        shift = target - a[0]
        if all((position + shift) % length in b for position in a):
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    main()
