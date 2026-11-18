import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    heights = data[1:n + 1]
    maximum = max(heights)
    stack = []

    for height in heights:
        if stack:
            if stack[-1] < height:
                print("NO")
                return
            if stack[-1] == height:
                stack.pop()
                continue
        stack.append(height)

    print("YES" if not stack or (len(stack) == 1 and stack[0] == maximum) else "NO")


if __name__ == "__main__":
    main()
