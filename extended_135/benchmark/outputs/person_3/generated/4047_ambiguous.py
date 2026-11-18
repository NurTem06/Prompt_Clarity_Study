import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    odd = sum(x & 1 for x in data[1:n + 1])
    print(min(odd, n - odd))

if __name__ == "__main__":
    main()
