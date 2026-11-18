import sys

def main():
    data = sys.stdin.buffer.read().split()
    s, t = data[0], data[1]
    n, m = len(s), len(t)

    left = [0] * m
    j = 0
    for i in range(n):
        if s[i] == t[j]:
            left[j] = i
            j += 1
            if j == m:
                break

    right = [0] * m
    j = m - 1
    for i in range(n - 1, -1, -1):
        if s[i] == t[j]:
            right[j] = i
            j -= 1
            if j < 0:
                break

    answer = max(right[0], n - left[-1] - 1)
    for i in range(m - 1):
        answer = max(answer, right[i + 1] - left[i] - 1)

    print(answer)

if __name__ == "__main__":
    main()
