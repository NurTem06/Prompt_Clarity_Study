import sys


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    required = list(map(int, input().split()))

    dependencies = [[] for _ in range(n + 1)]
    for course in range(1, n + 1):
        dependencies[course] = list(map(int, input().split()))[1:]

    state = bytearray(n + 1)
    position = [0] * (n + 1)
    order = []

    for root in required:
        if state[root] == 2:
            continue

        state[root] = 1
        stack = [root]

        while stack:
            course = stack[-1]
            index = position[course]

            if index == len(dependencies[course]):
                stack.pop()
                state[course] = 2
                order.append(course)
                continue

            prerequisite = dependencies[course][index]
            position[course] += 1

            if state[prerequisite] == 1:
                sys.stdout.write("-1\n")
                return

            if state[prerequisite] == 0:
                state[prerequisite] = 1
                stack.append(prerequisite)

    sys.stdout.write(str(len(order)) + "\n")
    sys.stdout.write(" ".join(map(str, order)) + "\n")


if __name__ == "__main__":
    main()