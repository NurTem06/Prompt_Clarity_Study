import sys


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    events = []
    coordinates = []

    for _ in range(n):
        m, day, left, right, height, dd, dx, dh = map(int, read().split())
        for _ in range(m):
            events.append((day, left, right, height))
            coordinates.append(left)
            coordinates.append(right)
            day += dd
            left += dx
            right += dx
            height += dh

    coordinates = sorted(set(coordinates))
    index = {x: i for i, x in enumerate(coordinates)}
    size = len(coordinates) - 1

    events = [
        (day, index[left], index[right] - 1, height)
        for day, left, right, height in events
    ]
    events.sort()
    del index, coordinates

    minimum = [0] * (4 * size)
    floor = [0] * (4 * size)

    def missed(node, lo, hi, left, right, height):
        if minimum[node] >= height:
            return False
        if left <= lo and hi <= right:
            return True

        mid = (lo + hi) >> 1
        child = node << 1
        if left <= mid and missed(child, lo, mid, left, right, height):
            return True
        if right > mid:
            return missed(child | 1, mid + 1, hi, left, right, height)
        return False

    def update(node, lo, hi, left, right, height):
        if minimum[node] >= height:
            return
        if left <= lo and hi <= right:
            minimum[node] = height
            floor[node] = height
            return

        mid = (lo + hi) >> 1
        child = node << 1
        if left <= mid:
            update(child, lo, mid, left, right, height)
        if right > mid:
            update(child | 1, mid + 1, hi, left, right, height)

        value = minimum[child]
        other = minimum[child | 1]
        if other < value:
            value = other
        if floor[node] > value:
            value = floor[node]
        minimum[node] = value

    answer = 0
    i = 0
    total = len(events)
    last = size - 1

    while i < total:
        j = i + 1
        day = events[i][0]
        while j < total and events[j][0] == day:
            j += 1

        pending = []
        for k in range(i, j):
            _, left, right, height = events[k]
            if missed(1, 0, last, left, right, height):
                answer += 1
                pending.append((left, right, height))

        for left, right, height in pending:
            update(1, 0, last, left, right, height)

        i = j

    print(answer)


if __name__ == "__main__":
    main()
