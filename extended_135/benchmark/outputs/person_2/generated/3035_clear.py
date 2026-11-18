import sys
import math

def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    best = {b"pink": 0.0}
    limit = math.log(10.0)

    for _ in range(n):
        offered, wanted, rate = read().split()
        current = best.get(wanted)
        if current is None:
            continue

        candidate = current + math.log(float(rate))
        previous = best.get(offered)
        if previous is None or candidate > previous:
            best[offered] = candidate
            if offered == b"blue" and candidate >= limit:
                print("10.000000000000000")
                return

    result = best.get(b"blue")
    amount = 0.0 if result is None else math.exp(result)
    print(f"{amount:.15f}")

if __name__ == "__main__":
    main()