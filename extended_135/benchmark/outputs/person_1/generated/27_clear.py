import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    answer = n
    for length in range(1, n // 2 + 1):
        if s[:length] == s[length:2 * length]:
            answer = min(answer, n - length + 1)
    print(answer)

if __name__ == "__main__":
    main()