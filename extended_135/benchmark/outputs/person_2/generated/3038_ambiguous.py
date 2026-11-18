import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    required = data[0]
    companies = data[1]
    pos = 2
    previous_sizes = None
    previous_contents = None
    answer = None

    for _ in range(companies):
        count = data[pos]
        pos += 1
        sizes = data[pos:pos + count]
        pos += count

        if previous_sizes is None:
            contents = [min(required, size) for size in sizes]
        else:
            limit = sizes[-1] + previous_sizes[0] - 1
            unreachable = required + 1
            dp = [unreachable] * (limit + 1)
            dp[0] = 0

            for size, actual in zip(previous_sizes, previous_contents):
                for total in range(size, limit + 1):
                    before = dp[total - size]
                    if before != unreachable:
                        candidate = min(required, before + actual)
                        if candidate < dp[total]:
                            dp[total] = candidate

            contents = [0] * count
            index = count - 1
            nearest_contents = unreachable
            for total in range(limit, -1, -1):
                if dp[total] != unreachable:
                    nearest_contents = dp[total]
                if index >= 0 and total == sizes[index]:
                    contents[index] = nearest_contents
                    index -= 1
                    if index < 0:
                        break

        for size, actual in zip(sizes, contents):
            if actual >= required and (answer is None or size < answer):
                answer = size

        previous_sizes = sizes
        previous_contents = contents

    print(answer if answer is not None else "impossible")


if __name__ == "__main__":
    main()