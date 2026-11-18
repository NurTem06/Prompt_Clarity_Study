import sys

def main():
    s, t = sys.stdin.buffer.read().split()
    n, m = len(s), len(t)

    left = [-1] * (m + 1)
    j = 0
    for i, c in enumerate(s):
        if j < m and c == t[j]:
            j += 1
            left[j] = i

    right = [n] * (m + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            right[j] = i
            j -= 1

    print(max(right[k] - left[k] - 1 for k in range(m + 1)))

if __name__ == "__main__":
    main()