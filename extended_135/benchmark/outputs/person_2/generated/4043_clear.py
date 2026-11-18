import sys


def main():
    n, d, k = map(int, sys.stdin.buffer.read().split())

    if d >= n:
        sys.stdout.write("NO\n")
        return

    if d == 1:
        sys.stdout.write("YES\n1 2\n" if n == 2 else "NO\n")
        return

    if k < 2 or (k == 2 and n != d + 1):
        sys.stdout.write("NO\n")
        return

    edges = [f"{i} {i + 1}\n" for i in range(1, d + 1)]
    count = d + 1

    if k > 2:
        for i in range(1, d):
            if count == n:
                break

            stack = [(i + 1, min(i, d - i), k - 2)]

            while stack and count < n:
                vertex, depth, slots = stack[-1]

                if slots == 1:
                    stack.pop()
                else:
                    stack[-1] = (vertex, depth, slots - 1)

                count += 1
                edges.append(f"{vertex} {count}\n")

                if depth > 1:
                    stack.append((count, depth - 1, k - 1))

    if count != n:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write("".join(edges))


if __name__ == "__main__":
    main()
