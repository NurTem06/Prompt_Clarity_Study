import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    out = []

    for i in range(1, len(data), 3):
        a, b, c = data[i:i + 3]

        r = c % a
        C = c - r if r <= a - r else c + a - r
        best = b - a + abs(C - c)
        answer = (a, a, C)

        r = c % b
        C = c - r if r <= b - r else c + b - r
        cost = a - 1 + abs(C - c)
        if cost < best:
            best = cost
            answer = (1, b, C)

        for A in range(max(1, a - best), a + best + 1):
            da = abs(A - a)
            if da >= best:
                continue

            remaining = best - da - 1
            low = max(1, (b - remaining + A - 1) // A)
            high = (b + remaining) // A

            for B in range(low * A, high * A + 1, A):
                partial = da + abs(B - b)
                if partial >= best:
                    continue

                if B > c:
                    C = B
                    distance = B - c
                else:
                    r = c % B
                    if r <= B - r:
                        C = c - r
                        distance = r
                    else:
                        C = c + B - r
                        distance = B - r

                cost = partial + distance
                if cost < best:
                    best = cost
                    answer = (A, B, C)

            if best == 0:
                break

        out.append(str(best))
        out.append("{} {} {}".format(*answer))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
