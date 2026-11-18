import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    adj = [[] for _ in range(n)]
    for i in range(1, len(data), 3):
        a, b, color = data[i], data[i + 1], data[i + 2]
        a -= 1
        b -= 1
        adj[a].append((b, color))
        adj[b].append((a, color))

    parent = [-1] * n
    tin = [0] * n
    order = []
    stack = [0]

    while stack:
        v = stack.pop()
        tin[v] = len(order)
        order.append(v)
        for u, _ in adj[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append(u)

    size = [1] * n
    for v in reversed(order):
        if parent[v] != -1:
            size[parent[v]] += size[v]

    diff = [0] * (n + 1)
    global_bad = 0

    for v in range(n):
        counts = {}
        for _, color in adj[v]:
            counts[color] = counts.get(color, 0) + 1

        for u, color in adj[v]:
            if counts[color] < 2:
                continue
            if u == parent[v]:
                global_bad += 1
                diff[tin[v]] -= 1
                diff[tin[v] + size[v]] += 1
            else:
                diff[tin[u]] += 1
                diff[tin[u] + size[u]] -= 1

    good = [False] * n
    bad = global_bad
    for i, v in enumerate(order):
        bad += diff[i]
        if bad == 0:
            good[v] = True

    answer = [str(v + 1) for v in range(n) if good[v]]
    sys.stdout.write("\n".join([str(len(answer))] + answer))


if __name__ == "__main__":
    main()
