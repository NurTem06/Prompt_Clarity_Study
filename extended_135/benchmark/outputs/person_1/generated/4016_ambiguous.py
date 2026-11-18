import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, k = map(int, data[:2])
    t = data[2].decode()

    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j

    print(t + t[pi[-1]:] * (k - 1))

if __name__ == "__main__":
    main()