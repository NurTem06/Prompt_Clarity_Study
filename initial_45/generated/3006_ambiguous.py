import sys


def read_program(lines):
    segments = [(1, 10**10 + 5000)]

    for line in lines:
        parts = line.split()
        if not parts:
            continue
        operation = parts[0]
        if operation == b'E':
            break

        offset = int(parts[1]) - 1
        index = 0
        while offset >= segments[index][1]:
            offset -= segments[index][1]
            index += 1

        start, length = segments[index]

        if operation == b'I':
            inserted = (-parts[2][0], 1)
            if offset == 0:
                segments.insert(index, inserted)
            else:
                segments[index:index + 1] = [
                    (start, offset),
                    inserted,
                    (start + offset, length - offset),
                ]
        else:
            replacement = []
            if offset:
                replacement.append((start, offset))
            if offset + 1 < length:
                replacement.append((start + offset + 1, length - offset - 1))
            segments[index:index + 1] = replacement

    canonical = []
    for start, length in segments:
        if (
            start > 0
            and canonical
            and canonical[-1][0] > 0
            and canonical[-1][0] + canonical[-1][1] == start
        ):
            previous_start, previous_length = canonical[-1]
            canonical[-1] = (previous_start, previous_length + length)
        else:
            canonical.append((start, length))
    return canonical


def main():
    lines = iter(sys.stdin.buffer)
    first = read_program(lines)
    second = read_program(lines)
    print(0 if first == second else 1)


if __name__ == "__main__":
    main()
