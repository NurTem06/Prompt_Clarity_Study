import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = sorted(data[1:n + 1])
    print(min(a[-1] - a[1], a[-2] - a[0]))

if __name__ == "__main__":
    main()
