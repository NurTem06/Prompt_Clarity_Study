import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    digits = bytearray(data[1])
    mapping = [0] + [int(x) + 48 for x in data[2:11]]

    started = False
    for i in range(n):
        original = digits[i]
        replacement = mapping[original - 48]
        if not started:
            if replacement > original:
                started = True
                digits[i] = replacement
        elif replacement >= original:
            digits[i] = replacement
        else:
            break

    sys.stdout.buffer.write(digits + b"\n")


if __name__ == "__main__":
    main()
