import sys


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))

    prerequisites = [[] for _ in range(n + 1)]
    for course in range(1, n + 1):
        prerequisites[course] = list(map(int, input().split()))[1:]

    state = bytearray(n + 1)
    order = []

    for root in main_courses:
        if state[root] == 2:
            continue

        stack = [root]
        while stack:
            course = stack.pop()

            if course < 0:
                course = -course
                state[course] = 2
                order.append(course)
                continue

            if state[course] == 2:
                continue
            if state[course] == 1:
                sys.stdout.write("-1\n")
                return

            state[course] = 1
            stack.append(-course)
            stack.extend(prerequisites[course])

    sys.stdout.write(str(len(order)) + "\n")
    sys.stdout.write(" ".join(map(str, order)) + "\n")


if __name__ == "__main__":
    main()
