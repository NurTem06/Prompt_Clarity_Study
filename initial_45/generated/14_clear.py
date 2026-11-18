import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    prefix = data[2:2 + k]

    used = bytearray(n + 1)
    stack = []
    expected = 1

    for x in prefix:
        if stack and stack[-1] < x:
            sys.stdout.write("-1\n")
            return

        used[x] = 1
        stack.append(x)

        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

    answer = [str(x) for x in prefix]
    stack.reverse()
    stack.append(n + 1)

    previous = 0
    for boundary in stack:
        for x in range(boundary - 1, previous, -1):
            if not used[x]:
                answer.append(str(x))
        previous = boundary

    sys.stdout.write(" ".join(answer) + "\n")


if __name__ == "__main__":
    main()
