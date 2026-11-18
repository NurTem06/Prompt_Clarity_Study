import sys

def main():
    data = sys.stdin.buffer.read().split()
    a = bytearray(data[1])
    mapping = [0] + [int(x) + 48 for x in data[2:11]]
    started = False

    for i, digit in enumerate(a):
        replacement = mapping[digit - 48]
        if not started:
            if replacement > digit:
                started = True
                a[i] = replacement
        else:
            if replacement < digit:
                break
            a[i] = replacement

    sys.stdout.buffer.write(a + b'\n')

if __name__ == "__main__":
    main()