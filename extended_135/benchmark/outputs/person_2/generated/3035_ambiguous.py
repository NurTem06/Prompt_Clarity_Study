import sys
import math


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    best = {b"pink": 0.0}

    for _ in range(n):
        offered, wanted, rate = data.readline().split()
        amount = best.get(wanted)
        if amount is not None:
            candidate = amount + math.log(float(rate))
            previous = best.get(offered)
            if previous is None or candidate > previous:
                best[offered] = candidate

    result = best.get(b"blue")
    if result is None:
        print("0.000000000000000")
    elif result >= math.log(10.0):
        print("10.000000000000000")
    else:
        print(f"{math.exp(result):.15f}")


if __name__ == "__main__":
    main()
