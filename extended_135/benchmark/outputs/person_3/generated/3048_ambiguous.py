import sys

def main():
    data = map(int, sys.stdin.buffer.read().split())
    n = next(data)
    degree = [0] * (n + 1)

    for _ in range(n - 1):
        u = next(data)
        v = next(data)
        degree[u] += 1
        degree[v] += 1

    print(sum(d * (d - 1) for d in degree))

if __name__ == "__main__":
    main()
