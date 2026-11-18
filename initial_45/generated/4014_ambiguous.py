import sys
import heapq


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    releases = [[] for _ in range(n + 1)]
    exam_day = [0] * (n + 1)
    remaining = [0] * (m + 1)

    pos = 2
    for i in range(1, m + 1):
        s, d, c = data[pos:pos + 3]
        pos += 3
        releases[s].append((d, i))
        exam_day[d] = i
        remaining[i] = c

    heap = []
    plan = []

    for day in range(1, n + 1):
        for exam in releases[day]:
            heapq.heappush(heap, exam)

        i = exam_day[day]
        if i:
            if remaining[i]:
                print(-1)
                return
            plan.append(m + 1)
        elif heap:
            deadline, i = heapq.heappop(heap)
            if deadline <= day:
                print(-1)
                return
            plan.append(i)
            remaining[i] -= 1
            if remaining[i]:
                heapq.heappush(heap, (deadline, i))
        else:
            plan.append(0)

    if any(remaining):
        print(-1)
    else:
        print(*plan)


if __name__ == "__main__":
    main()