import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    adj = [[] for _ in range(n)]
    for i in range(1, len(data), 3):
        a, b, color = data[i] - 1, data[i + 1] - 1, data[i + 2]
        adj[a].append((b, color))
        adj[b].append((a, color))

    parent = [-1] * n
    order = [0]
    for v in order:
        for u, _ in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    delta = [0] * n
    base = 0

    for v in range(n):
        counts = {}
        for _, color in adj[v]:
            counts[color] = counts.get(color, 0) + 1

        for u, color in adj[v]:
            if counts[color] > 1:
                if u == parent[v]:
                    base += 1
                    delta[v] -= 1
                else:
                    delta[u] += 1

    delta[0] += base
    for v in order[1:]:
        delta[v] += delta[parent[v]]

    answer = [str(v + 1) for v in range(n) if delta[v] == 0]
    sys.stdout.write("\n".join([str(len(answer))] + answer) + "\n")


if __name__ == "__main__":
    main()
