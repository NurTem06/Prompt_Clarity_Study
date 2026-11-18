import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, x, y = map(int, data[:3])
    s = data[3]
    ones = s[n - x:].count(b'1')
    print(ones + (1 if s[n - y - 1] == 48 else -1))

if __name__ == "__main__":
    main()
