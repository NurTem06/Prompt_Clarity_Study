import sys


def solve_case(a, b, c):
    best = 10**9
    answer = (a, a, a)

    for A, B in (
        (1, b),
        (a, a),
        (a, (b // a) * a),
        (a, (b // a + 1) * a),
        (b, b),
    ):
        C = max(1, (c + B // 2) // B) * B
        cost = abs(a - A) + abs(b - B) + abs(c - C)
        if cost < best:
            best = cost
            answer = (A, B, C)

    if best == 0:
        return best, answer

    lower_a = max(1, a - best + 1)
    upper_a = a + best

    for A in range(lower_a, upper_a):
        da = abs(a - A)
        remaining = best - da - 1
        if remaining < 0:
            continue

        lower_b = max(A, b - remaining)
        first_b = ((lower_b + A - 1) // A) * A
        upper_b = b + remaining

        for B in range(first_b, upper_b + 1, A):
            partial = da + abs(b - B)
            if partial >= best:
                continue

            C = max(1, (c + B // 2) // B) * B
            cost = partial + abs(c - C)
            if cost < best:
                best = cost
                answer = (A, B, C)
                if best == 0:
                    return best, answer

    return best, answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    output = []
    pos = 1
    for _ in range(data[0]):
        a, b, c = data[pos:pos + 3]
        pos += 3
        cost, triple = solve_case(a, b, c)
        output.append(str(cost))
        output.append("{} {} {}".format(*triple))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()