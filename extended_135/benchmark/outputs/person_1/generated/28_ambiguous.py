import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    files = []
    examples = 0
    occupied = bytearray(n + 1)

    for i in range(n):
        name = data[2 * i + 1].decode()
        kind = int(data[2 * i + 2])
        examples += kind

        position = 0
        if name.isdigit():
            value = int(name)
            if 1 <= value <= n and str(value) == name:
                position = value
                occupied[value] = 1

        files.append((name, kind, position))

    inside = [[], []]
    outside = [[], []]
    holes = [[], []]

    for name, kind, position in files:
        if position == 0:
            outside[kind].append(name)
        else:
            required_kind = 1 if position <= examples else 0
            if kind != required_kind:
                inside[kind].append(name)

    for position in range(1, n + 1):
        if not occupied[position]:
            kind = 1 if position <= examples else 0
            holes[kind].append(position)

    commands = []

    if not holes[0] and not holes[1] and (inside[0] or inside[1]):
        kind = 0 if inside[0] else 1
        source = inside[kind].pop()
        temporary = str(n + 1)
        commands.append(f"move {source} {temporary}")
        outside[kind].append(temporary)
        holes[1 - kind].append(int(source))

    while holes[0] or holes[1]:
        kind = 0 if holes[0] else 1
        destination = holes[kind].pop()

        if inside[kind]:
            source = inside[kind].pop()
            holes[1 - kind].append(int(source))
        else:
            source = outside[kind].pop()

        commands.append(f"move {source} {destination}")

    sys.stdout.write(str(len(commands)) + "\n")
    if commands:
        sys.stdout.write("\n".join(commands) + "\n")


if __name__ == "__main__":
    main()
