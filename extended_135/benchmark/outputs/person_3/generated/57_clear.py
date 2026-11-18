import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    xs = data[1:2 * n + 1:2]
    ys = data[2:2 * n + 1:2]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    print(width * height if width and height else -1)

if __name__ == "__main__":
    main()