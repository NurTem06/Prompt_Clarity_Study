import sys

def intersection_area(*rectangles):
    left = max(r[0] for r in rectangles)
    bottom = max(r[1] for r in rectangles)
    right = min(r[2] for r in rectangles)
    top = min(r[3] for r in rectangles)
    return max(0, right - left) * max(0, top - bottom)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    white = data[:4]
    black1 = data[4:8]
    black2 = data[8:12]

    total = (white[2] - white[0]) * (white[3] - white[1])
    covered = (
        intersection_area(white, black1)
        + intersection_area(white, black2)
        - intersection_area(white, black1, black2)
    )
    print("YES" if covered < total else "NO")

if __name__ == "__main__":
    main()