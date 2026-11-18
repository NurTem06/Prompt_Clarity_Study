import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    changed = False
    increasing = False
    previous = 4127

    for i in range(n):
        a, b = data[2 * i + 1], data[2 * i + 2]
        if a != b:
            changed = True
        if a > previous:
            increasing = True
        previous = a

    print("rated" if changed else "unrated" if increasing else "maybe")

if __name__ == "__main__":
    main()