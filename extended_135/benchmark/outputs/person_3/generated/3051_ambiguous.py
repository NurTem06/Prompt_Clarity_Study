import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    events = []
    coordinates = set()
    pos = 1

    for _ in range(data[0]):
        m, day, left, right, height, dd, dx, dh = data[pos:pos + 8]
        pos += 8

        for _ in range(m):
            events.append((day, left, right, height))
            coordinates.add(left)
            coordinates.add(right)
            day += dd
            left += dx
            right += dx
            height += dh

    del data
    events.sort()
    coordinates = sorted(coordinates)
    index = {x: i for i, x in enumerate(coordinates)}
    size = len(coordinates) - 1

    minimum = [0] * (4 * size + 4)
    floor = [0] * (4 * size + 4)

    def missed(node, lo, hi, ql, qr, height):
        if minimum[node] >= height:
            return False
        if ql <= lo and hi <= qr:
            return True

        mid = (lo + hi) // 2
        if ql < mid and missed(node * 2, lo, mid, ql, qr, height):
            return True
        if qr > mid and missed(node * 2 + 1, mid, hi, ql, qr, height):
            return True
        return False

    def extend(node, lo, hi, ql, qr, height):
        if minimum[node] >= height:
            return
        if ql <= lo and hi <= qr:
            minimum[node] = height
            floor[node] = height
            return

        mid = (lo + hi) // 2
        child = node * 2
        if ql < mid:
            extend(child, lo, mid, ql, qr, height)
        if qr > mid:
            extend(child + 1, mid, hi, ql, qr, height)

        value = minimum[child]
        if minimum[child + 1] < value:
            value = minimum[child + 1]
        if floor[node] > value:
            value = floor[node]
        minimum[node] = value

    answer = 0
    i = 0
    count = len(events)

    while i < count:
        day = events[i][0]
        pending = []

        while i < count and events[i][0] == day:
            _, left, right, height = events[i]
            left = index[left]
            right = index[right]
            if missed(1, 0, size, left, right, height):
                answer += 1
                pending.append((left, right, height))
            i += 1

        for left, right, height in pending:
            extend(1, 0, size, left, right, height)

    print(answer)


if __name__ == "__main__":
    main()