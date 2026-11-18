import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    strings = sorted(data[1:n + 1], key=len)

    for i in range(1, n):
        if strings[i - 1] not in strings[i]:
            sys.stdout.write("NO\n")
            return

    sys.stdout.buffer.write(b"YES\n" + b"\n".join(strings) + b"\n")


if __name__ == "__main__":
    main()