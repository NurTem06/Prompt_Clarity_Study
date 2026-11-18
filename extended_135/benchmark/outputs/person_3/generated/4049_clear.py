import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:4]
    b = data[4:7]

    minimum = max(0, a[0] + b[1] - n,
                  a[1] + b[2] - n, a[2] + b[0] - n)
    maximum = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])

    print(minimum, maximum)

if __name__ == "__main__":
    main()