import sys

def main():
    d, k, a, b, t = map(int, sys.stdin.buffer.read().split())

    first = min(d, k)
    answer = first * a
    remaining = d - first

    if t >= k * (b - a):
        answer += remaining * b
    else:
        blocks, rest = divmod(remaining, k)
        answer += blocks * (t + k * a)
        answer += min(rest * b, t + rest * a)

    print(answer)

if __name__ == "__main__":
    main()