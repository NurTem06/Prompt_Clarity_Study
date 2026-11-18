import sys
from itertools import permutations

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1].decode()
    t = data[2].decode()

    for p in permutations("abc"):
        for res in ("".join(p) * n, "".join(c * n for c in p)):
            if s not in res and t not in res:
                sys.stdout.write("YES\n" + res + "\n")
                return

    sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()