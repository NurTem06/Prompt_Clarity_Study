import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    required, companies = data[0], data[1]
    pos = 2
    previous_sizes = None
    previous_actual = None
    answer = None
    unreachable = required + 1

    for _ in range(companies):
        count = data[pos]
        pos += 1
        sizes = data[pos:pos + count]
        pos += count

        if previous_sizes is None:
            actual = [min(required, size) for size in sizes]
        else:
            limit = sizes[-1] + previous_sizes[0] - 1
            dp = [unreachable] * (limit + 1)
            dp[0] = 0
            packs = list(zip(previous_sizes, previous_actual))

            for total in range(1, limit + 1):
                best = unreachable
                for size, contents in packs:
                    if size > total:
                        break
                    earlier = dp[total - size]
                    if earlier != unreachable:
                        candidate = min(required, earlier + contents)
                        if candidate < best:
                            best = candidate
                dp[total] = best

            actual = []
            for target in sizes:
                total = target
                while dp[total] == unreachable:
                    total += 1
                actual.append(dp[total])

        for size, contents in zip(sizes, actual):
            if contents >= required and (answer is None or size < answer):
                answer = size

        previous_sizes = sizes
        previous_actual = actual

    print(answer if answer is not None else "impossible")


if __name__ == "__main__":
    main()
