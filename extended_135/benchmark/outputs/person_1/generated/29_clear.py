import sys

def main():
    digits = list(map(int, sys.stdin.buffer.read().strip().decode()))
    left = sum(digits[:3])
    right = sum(digits[3:])
    if left < right:
        gains = [9 - d for d in digits[:3]] + digits[3:]
    else:
        gains = digits[:3] + [9 - d for d in digits[3:]]

    difference = abs(left - right)
    changes = 0
    for gain in sorted(gains, reverse=True):
        if difference <= 0:
            break
        difference -= gain
        changes += 1
    print(changes)

if __name__ == "__main__":
    main()