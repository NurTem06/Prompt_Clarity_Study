import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    answer = n
    for k in range(1, n // 2 + 1):
        if s[:k] == s[k:2 * k]:
            answer = min(answer, n - k + 1)
    print(answer)

if __name__ == "__main__":
    main()
