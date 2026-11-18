import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    m = next(data)
    d = next(data)

    adj = [[] for _ in range(n + 1)]
    neighbors = []

    for _ in range(m):
        u = next(data)
        v = next(data)
        if u == 1:
            neighbors.append(v)
        elif v == 1:
            neighbors.append(u)
        else:
            adj[u].append(v)
            adj[v].append(u)

    if len(neighbors) < d:
        sys.stdout.write("NO\n")
        return

    seen = bytearray(n + 1)
    roots = []

    for start in neighbors:
        if seen[start]:
            continue

        roots.append(start)
        if len(roots) > d:
            sys.stdout.write("NO\n")
            return

        seen[start] = 1
        stack = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = 1
                    stack.append(v)

    seen = bytearray(n + 1)
    for v in roots:
        seen[v] = 1

    for v in neighbors:
        if len(roots) == d:
            break
        if not seen[v]:
            roots.append(v)
            seen[v] = 1

    answer = ["YES"]
    for v in roots:
        answer.append(f"1 {v}")

    stack = roots
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not seen[v]:
                seen[v] = 1
                answer.append(f"{u} {v}")
                stack.append(v)

    sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
