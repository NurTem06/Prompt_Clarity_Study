import sys

def main():
    d, k, a, b, t = map(int, sys.stdin.buffer.read().split())

    first = min(d, k)
    answer = first * a + (d - first) * b

    repairs = (d - 1) // k
    answer = min(answer, d * a + repairs * t)

    if repairs > 0:
        driven = repairs * k
        answer = min(
            answer,
            driven * a + (repairs - 1) * t + (d - driven) * b
        )

    print(answer)

if __name__ == "__main__":
    main()