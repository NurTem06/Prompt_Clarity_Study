import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    files = []
    names = set()
    examples = 0

    for i in range(n):
        name = data[1 + 2 * i].decode()
        kind = int(data[2 + 2 * i])
        files.append((name, kind))
        names.add(name)
        examples += kind

    internal = [[], []]
    external = [[], []]
    occupied = bytearray(n + 1)

    for name, kind in files:
        index = int(name) if name.isdigit() else 0
        if 1 <= index <= n and str(index) == name:
            occupied[index] = 1
            required = 1 if index <= examples else 0
            if kind != required:
                internal[kind].append(name)
        else:
            external[kind].append(name)

    holes = [[], []]
    for index in range(1, n + 1):
        if not occupied[index]:
            kind = 1 if index <= examples else 0
            holes[kind].append(str(index))

    temporary_index = n + 1
    while str(temporary_index) in names:
        temporary_index += 1
    temporary = str(temporary_index)

    operations = []

    while True:
        if holes[0] or holes[1]:
            kind = 1 if holes[1] else 0
            destination = holes[kind].pop()

            if internal[kind]:
                source = internal[kind].pop()
                holes[1 - kind].append(source)
            else:
                source = external[kind].pop()

            operations.append("move " + source + " " + destination)
        elif internal[0] or internal[1]:
            kind = 1 if internal[1] else 0
            source = internal[kind].pop()
            operations.append("move " + source + " " + temporary)
            external[kind].append(temporary)
            holes[1 - kind].append(source)
        else:
            break

    sys.stdout.write(str(len(operations)) + "\n")
    if operations:
        sys.stdout.write("\n".join(operations) + "\n")


if __name__ == "__main__":
    main()
