import sys

def main():
    w, m = map(int, sys.stdin.buffer.read().split())
    while m:
        remainder = m % w
        if remainder == 0 or remainder == 1:
            m //= w
        elif remainder == w - 1:
            m = (m + 1) // w
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()