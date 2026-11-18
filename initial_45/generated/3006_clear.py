import sys


def read_program(stream):
    segments = [(1, 10**10 + 4001)]

    while True:
        line = stream.readline()
        if not line:
            break
        fields = line.split()
        if not fields:
            continue
        operation = fields[0]
        if operation == b'E':
            break

        offset = int(fields[1]) - 1
        index = 0
        while offset >= segments[index][1]:
            offset -= segments[index][1]
            index += 1

        start, length = segments[index]
        replacement = []

        if offset:
            replacement.append((start, offset))

        if operation == b'I':
            replacement.append((-fields[2][0], 1))
            consumed = offset
        else:
            consumed = offset + 1

        if consumed < length:
            suffix_start = start + consumed if start > 0 else start
            replacement.append((suffix_start, length - consumed))

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
    stream = sys.stdin.buffer
    first = read_program(stream)
    second = read_program(stream)
    print(0 if first == second else 1)


if __name__ == "__main__":
    main()