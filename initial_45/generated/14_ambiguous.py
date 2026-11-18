import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    prefix = data[2:2 + k]

    stack = []
    needed = 1

    for x in prefix:
        if stack and x > stack[-1]:
            sys.stdout.write("-1\n")
            return

        stack.append(x)
        while stack and stack[-1] == needed:
            stack.pop()
            needed += 1

    answer = prefix
    lower = needed

    for boundary in reversed(stack):
        answer.extend(range(boundary - 1, lower - 1, -1))
        lower = boundary + 1

    answer.extend(range(n, lower - 1, -1))
    sys.stdout.write(" ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()