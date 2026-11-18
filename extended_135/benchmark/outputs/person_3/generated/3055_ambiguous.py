import sys

def main():
    lines = sys.stdin.read().split()
    n = int(lines[0])
    names = lines[1:n + 1]
    target = "ThoreHusfeldt"
    pos = names.index(target)

    if pos == 0:
        print("Thore is awesome")
        return

    above = names[:pos]
    if any(name.startswith(target[:-1]) for name in above):
        print("Thore sucks")
        return

    for length in range(1, len(target) + 1):
        prefix = target[:length]
        if not any(name.startswith(prefix) for name in above):
            print(prefix)
            return

if __name__ == "__main__":
    main()