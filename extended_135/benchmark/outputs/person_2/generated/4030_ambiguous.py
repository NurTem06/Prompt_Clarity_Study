import sys

def main():
    data = sys.stdin.buffer.read().split()
    s = data[1]
    dp = [0] * 27
    colors = []
    result = 0

    for ch in s:
        x = ch - 97
        color = max(dp[x + 1:]) + 1
        dp[x] = color
        colors.append(str(color))
        if color > result:
            result = color

    sys.stdout.write(str(result) + "\n" + " ".join(colors) + "\n")

if __name__ == "__main__":
    main()