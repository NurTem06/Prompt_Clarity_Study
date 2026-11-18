import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    r = int(data[1])
    m = int(data[2])

    times = []
    probabilities = []
    delays = []
    pos = 3

    for _ in range(m):
        times.append(int(data[pos]))
        probabilities.append(float(data[pos + 1]))
        delays.append(int(data[pos + 2]))
        pos += 3

    max_delay = r - n - 1
    limits = []
    accumulated = 0
    for d in delays:
        limits.append(min(max_delay, accumulated))
        accumulated += d

    terminal_size = min(max_delay, accumulated) + 1

    stages = []
    for i in range(m - 1, -1, -1):
        gap = (times[i + 1] if i + 1 < m else n) - times[i]
        stages.append((
            probabilities[i],
            1.0 - probabilities[i],
            delays[i],
            gap,
            limits[i] + 1,
        ))

    low = float(n)
    high = float(r * 50000)
    first_time = times[0]

    for _ in range(65):
        estimate = (low + high) * 0.5
        following = [0.0] * terminal_size

        for p, q, delay, gap, size in stages:
            current = [0.0] * size
            recoverable = min(size, max_delay - delay + 1)
            if recoverable < 0:
                recoverable = 0
            recovery_cost = delay + gap

            for s in range(recoverable):
                success = gap + following[s]
                if success > estimate:
                    success = estimate

                failure = recovery_cost + following[s + delay]
                if failure > estimate:
                    failure = estimate

                current[s] = p * success + q * failure

            reset_part = q * estimate
            for s in range(recoverable, size):
                success = gap + following[s]
                if success > estimate:
                    success = estimate
                current[s] = p * success + reset_part

            following = current

        if first_time + following[0] > estimate:
            low = estimate
        else:
            high = estimate

    print(f"{(low + high) * 0.5:.10f}")


if __name__ == "__main__":
    main()
