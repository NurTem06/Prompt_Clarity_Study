import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    print("YES" if all(abs(a[i] - a[i - 1]) <= 1 for i in range(1, n)) else "NO")

if __name__ == "__main__":
    main()