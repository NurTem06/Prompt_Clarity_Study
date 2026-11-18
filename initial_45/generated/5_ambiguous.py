import sys

def main():
    n, pos, l, r = map(int, sys.stdin.buffer.read().split())
    if l == 1 and r == n:
        answer = 0
    elif l == 1:
        answer = abs(pos - r) + 1
    elif r == n:
        answer = abs(pos - l) + 1
    else:
        answer = min(abs(pos - l), abs(pos - r)) + r - l + 2
    print(answer)

if __name__ == "__main__":
    main()