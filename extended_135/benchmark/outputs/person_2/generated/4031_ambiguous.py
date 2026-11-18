import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    strings = sorted(data[1:n + 1], key=len)

    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            sys.stdout.write("NO\n")
            return

    sys.stdout.buffer.write(b"YES\n" + b"\n".join(strings) + b"\n")

if __name__ == "__main__":
    main()
