import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    a = values[1:4]
    b = values[4:7]

    minimum = max(0, *(a[i] + b[(i + 1) % 3] - n for i in range(3)))
    maximum = sum(min(a[i], b[(i + 1) % 3]) for i in range(3))
    print(minimum, maximum)

if __name__ == "__main__":
    main()