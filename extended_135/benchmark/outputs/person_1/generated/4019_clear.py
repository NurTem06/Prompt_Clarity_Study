import sys


def main():
    data = map(int, sys.stdin.buffer.read().split())
    n = next(data)
    m = next(data)
    d = next(data)

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(data)
        v = next(data)
        graph[u].append(v)
        graph[v].append(u)

    if len(graph[1]) < d:
        sys.stdout.write("NO\n")
        return

    seen = bytearray(n + 1)
    seen[1] = 1
    selected = bytearray(n + 1)
    roots = []

    for start in graph[1]:
        if seen[start]:
            continue

        roots.append(start)
        selected[start] = 1
        if len(roots) > d:
            sys.stdout.write("NO\n")
            return

        seen[start] = 1
        stack = [start]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = 1
                    stack.append(v)

    for v in graph[1]:
        if len(roots) == d:
            break
        if not selected[v]:
            selected[v] = 1
            roots.append(v)

    seen = bytearray(n + 1)
    seen[1] = 1
    output = ["YES"]
    for v in roots:
        seen[v] = 1
        output.append(f"1 {v}")

    stack = roots
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not seen[v]:
                seen[v] = 1
                output.append(f"{u} {v}")
                stack.append(v)

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
