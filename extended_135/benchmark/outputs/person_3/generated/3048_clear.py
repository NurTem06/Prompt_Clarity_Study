import sys

def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    degree = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, read().split())
        degree[u] += 1
        degree[v] += 1

    print(sum(d * (d - 1) for d in degree))

if __name__ == "__main__":
    main()
