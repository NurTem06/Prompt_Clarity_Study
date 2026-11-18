import sys

def main():
    digits = list(map(int, sys.stdin.buffer.read().strip().decode()))
    left, right = digits[:3], digits[3:]
    difference = sum(left) - sum(right)

    if difference < 0:
        left, right = right, left
        difference = -difference

    gains = sorted(left + [9 - digit for digit in right], reverse=True)
    changes = 0
    for gain in gains:
        if difference <= 0:
            break
        difference -= gain
        changes += 1

    print(changes)

if __name__ == "__main__":
    main()
