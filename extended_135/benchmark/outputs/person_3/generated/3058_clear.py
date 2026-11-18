import sys


def is_subsequence(shorter, longer):
    if len(shorter) > len(longer):
        return False
    it = iter(longer)
    return all(c in it for c in shorter)


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    current = data[1]
    fossils = sorted(data[2:2 + n], key=len, reverse=True)

    first = []
    second = []
    pending = []
    head_first = current
    head_second = current

    for sequence in fossils:
        if pending:
            if is_subsequence(sequence, pending[-1]):
                pending.append(sequence)
                continue

            if is_subsequence(sequence, head_first):
                second.extend(pending)
                head_second = pending[-1]
                first.append(sequence)
                head_first = sequence
            elif is_subsequence(sequence, head_second):
                first.extend(pending)
                head_first = pending[-1]
                second.append(sequence)
                head_second = sequence
            else:
                sys.stdout.buffer.write(b"impossible\n")
                return

            pending = []
        else:
            fits_first = is_subsequence(sequence, head_first)
            fits_second = is_subsequence(sequence, head_second)

            if fits_first and fits_second:
                pending.append(sequence)
            elif fits_first:
                first.append(sequence)
                head_first = sequence
            elif fits_second:
                second.append(sequence)
                head_second = sequence
            else:
                sys.stdout.buffer.write(b"impossible\n")
                return

    first.extend(pending)
    output = [f"{len(first)} {len(second)}".encode()]
    output.extend(reversed(first))
    output.extend(reversed(second))
    sys.stdout.buffer.write(b"\n".join(output) + b"\n")


if __name__ == "__main__":
    main()