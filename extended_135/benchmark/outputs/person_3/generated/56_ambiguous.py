import sys

def main():
    n, t = map(int, sys.stdin.buffer.read().split())
    row = [float(t)]
    full = 0

    for level in range(n):
        next_row = [0.0] * (level + 2)
        for j, amount in enumerate(row):
            if amount >= 1.0:
                full += 1
                overflow = (amount - 1.0) / 2.0
                next_row[j] += overflow
                next_row[j + 1] += overflow
        row = next_row

    print(full)

if __name__ == "__main__":
    main()