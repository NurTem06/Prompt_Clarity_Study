import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:2 + n]

    left, right = 0, n - 1
    while left <= right and a[left] <= k:
        left += 1
    while left <= right and a[right] <= k:
        right -= 1

    print(left + n - 1 - right)

if __name__ == "__main__":
    main()