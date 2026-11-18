import sys

def main():
    n, m = map(int, sys.stdin.buffer.read().split())
    a = [n // 5] * 5
    b = [m // 5] * 5
    for r in range(1, n % 5 + 1):
        a[r] += 1
    for r in range(1, m % 5 + 1):
        b[r] += 1
    print(sum(a[r] * b[(-r) % 5] for r in range(5)))

if __name__ == "__main__":
    main()