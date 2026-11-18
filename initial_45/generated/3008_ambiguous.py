import sys
from bisect import bisect_right


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + 2 * n]
    del data

    order_a = sorted(range(n), key=a.__getitem__)
    order_b = sorted(range(n), key=b.__getitem__)

    pos_a = [0] * n
    pos_b = [0] * n
    for i, v in enumerate(order_a):
        pos_a[v] = i
    for i, v in enumerate(order_b):
        pos_b[v] = i

    values_a = [a[v] for v in order_a]
    values_b = [b[v] for v in order_b]
    limit_a = [bisect_right(values_a, x + k) for x in a]
    limit_b = [bisect_right(values_b, x + k) for x in b]
    del values_a, values_b

    parent_a = list(range(n + 1))
    parent_b = list(range(n + 1))
    seen = bytearray(n)
    finish = []

    for root in range(n):
        if seen[root]:
            continue

        seen[root] = 1
        p = pos_a[root]
        parent_a[p] = find(parent_a, p + 1)
        p = pos_b[root]
        parent_b[p] = find(parent_b, p + 1)
        stack = [root]

        while stack:
            v = stack[-1]
            p = find(parent_a, limit_a[v])
            if p < n:
                u = order_a[p]
            else:
                p = find(parent_b, limit_b[v])
                if p == n:
                    finish.append(stack.pop())
                    continue
                u = order_b[p]

            seen[u] = 1
            p = pos_a[u]
            parent_a[p] = find(parent_a, p + 1)
            p = pos_b[u]
            parent_b[p] = find(parent_b, p + 1)
            stack.append(u)

    del parent_a, parent_b, pos_a, pos_b, limit_a, limit_b

    seen = bytearray(n)
    pointer_a = 0
    pointer_b = 0
    answer = 0

    for root in reversed(finish):
        if seen[root]:
            continue

        answer += 1
        seen[root] = 1
        stack = [root]

        while stack:
            v = stack.pop()
            threshold = a[v] - k
            while pointer_a < n:
                u = order_a[pointer_a]
                if seen[u]:
                    pointer_a += 1
                elif a[u] < threshold:
                    seen[u] = 1
                    stack.append(u)
                    pointer_a += 1
                else:
                    break

            threshold = b[v] - k
            while pointer_b < n:
                u = order_b[pointer_b]
                if seen[u]:
                    pointer_b += 1
                elif b[u] < threshold:
                    seen[u] = 1
                    stack.append(u)
                    pointer_b += 1
                else:
                    break

    print(answer)


if __name__ == "__main__":
    main()
