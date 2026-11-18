import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    r = int(data[1])
    m = int(data[2])

    tricks = []
    pos = 3
    for _ in range(m):
        t = int(data[pos])
        p = float(data[pos + 1])
        d = int(data[pos + 2])
        tricks.append((t, p, d))
        pos += 3

    states = r - n
    steps = []
    next_time = n
    for t, p, d in reversed(tricks):
        steps.append((next_time - t, p, 1.0 - p, d))
        next_time = t

    first_time = tricks[0][0]
    low = float(n)
    high = float(r * 50000)

    for _ in range(60):
        estimate = (low + high) * 0.5
        following = [0.0] * states

        for gap, p, q, delay in steps:
            current = [0.0] * states
            valid = max(0, states - delay)

            for extra in range(valid):
                success = gap + following[extra]
                if success > estimate:
                    success = estimate

                failure = delay + gap + following[extra + delay]
                if failure > estimate:
                    failure = estimate

                current[extra] = p * success + q * failure

            reset_part = q * estimate
            for extra in range(valid, states):
                success = gap + following[extra]
                if success > estimate:
                    success = estimate
                current[extra] = p * success + reset_part

            following = current

        if first_time + following[0] > estimate:
            low = estimate
        else:
            high = estimate

    print(f"{(low + high) * 0.5:.12f}")


if __name__ == "__main__":
    main()
