import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:n + 1]
    changes = 0

    for i in range(1, n - 1):
        if a[i - 1] == 1 and a[i] == 0 and a[i + 1] == 1:
            a[i + 1] = 0
            changes += 1

    print(changes)

if __name__ == "__main__":
    main()