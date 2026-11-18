import sys


def intersection(a, b):
    return (
        max(a[0], b[0]),
        max(a[1], b[1]),
        min(a[2], b[2]),
        min(a[3], b[3]),
    )


def area(r):
    return max(0, r[2] - r[0]) * max(0, r[3] - r[1])


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    white = values[:4]
    black1 = values[4:8]
    black2 = values[8:12]

    covered1 = intersection(white, black1)
    covered2 = intersection(white, black2)
    covered_area = (
        area(covered1)
        + area(covered2)
        - area(intersection(covered1, covered2))
    )
    print("YES" if covered_area < area(white) else "NO")


if __name__ == "__main__":
    main()