import sys


def main():
    n, m, k = map(int, sys.stdin.buffer.read().split())
    if n > m:
        n, m = m, n

    if n == 1:
        print(k)
        return
    if k == n * m:
        print(k)
        return

    low = (k + m - 1) // m
    high = k

    while low < high:
        mid = (low + high) // 2
        full_rows = min(n, mid // m)
        count = full_rows * m
        limit = min(n, mid)

        for i in range(full_rows + 1, limit + 1):
            count += mid // i

        if count >= k:
            high = mid
        else:
            low = mid + 1

    print(low)


if __name__ == "__main__":
    main()