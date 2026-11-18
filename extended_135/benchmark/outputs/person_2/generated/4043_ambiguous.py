import sys


def main():
    n, d, k = map(int, sys.stdin.buffer.readline().split())

    if d >= n or (k == 1 and (n != 2 or d != 1)):
        sys.stdout.write("NO\n")
        return

    if k == 2 and n != d + 1:
        sys.stdout.write("NO\n")
        return

    edges = [f"{i} {i + 1}\n" for i in range(1, d + 1)]
    next_vertex = d + 2

    if next_vertex <= n:
        stack = [
            (i + 1, min(i, d - i))
            for i in range(1, d)
        ] if k > 2 else []

        while stack and next_vertex <= n:
            parent, budget = stack.pop()
            slots = k - 2 if parent <= d + 1 else k - 1
            count = min(slots, n - next_vertex + 1)

            for _ in range(count):
                child = next_vertex
                next_vertex += 1
                edges.append(f"{parent} {child}\n")
                if budget > 1:
                    stack.append((child, budget - 1))

        if next_vertex <= n:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")
    sys.stdout.write("".join(edges))


if __name__ == "__main__":
    main()
