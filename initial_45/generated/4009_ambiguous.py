import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, x, y = map(int, data[:3])
    s = data[3]
    ones = s[-x:].count(b'1')
    target_is_one = s[n - y - 1] == ord('1')
    print(ones - 1 if target_is_one else ones + 1)

if __name__ == "__main__":
    main()
