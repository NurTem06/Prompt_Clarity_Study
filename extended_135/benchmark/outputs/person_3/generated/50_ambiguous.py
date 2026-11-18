import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, r = data[:3]
    buy = min(data[3:3 + n])
    sell = max(data[3 + n:3 + n + m])
    print(max(r, (r // buy) * sell + r % buy))

if __name__ == "__main__":
    main()