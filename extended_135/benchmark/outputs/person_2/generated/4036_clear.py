import sys


def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    minimum = k * (k + 1) // 2
    if n < minimum:
        print("NO")
        return

    extra, remaining = divmod(n - minimum, k)
    a = [i + extra for i in range(1, k + 1)]

    for i in range(k - 1, 0, -1):
        if remaining == 0:
            break
        limit = 2 * a[i - 1]
        if i + 1 < k:
            limit = min(limit, a[i + 1] - 1)
        take = min(remaining, limit - a[i])
        a[i] += take
        remaining -= take

    if remaining:
        print("NO")
    else:
        print("YES")
        print(*a)


if __name__ == "__main__":
    main()
