import sys


def is_subsequence(s, t):
    if len(s) >= len(t):
        return s == t
    it = iter(t)
    return all(c in it for c in s)


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    current = data.readline().strip()
    fossils = [data.readline().strip() for _ in range(n)]
    fossils.sort(key=len, reverse=True)

    first = []
    second = []
    pending = []
    a = b = current

    for s in fossils:
        if pending and is_subsequence(s, pending[-1]):
            pending.append(s)
            continue

        fits_a = is_subsequence(s, a)
        fits_b = fits_a if a is b else is_subsequence(s, b)

        if not fits_a and not fits_b:
            sys.stdout.write("impossible\n")
            return

        if pending:
            if fits_a:
                first.append(s)
                second.extend(pending)
                a, b = s, pending[-1]
            else:
                first.extend(pending)
                second.append(s)
                a, b = pending[-1], s
            pending = []
        elif fits_a and fits_b:
            pending.append(s)
        elif fits_a:
            first.append(s)
            a = s
        else:
            second.append(s)
            b = s

    first.extend(pending)

    output = [f"{len(first)} {len(second)}".encode()]
    output.extend(reversed(first))
    output.extend(reversed(second))
    sys.stdout.buffer.write(b"\n".join(output) + b"\n")


if __name__ == "__main__":
    main()
