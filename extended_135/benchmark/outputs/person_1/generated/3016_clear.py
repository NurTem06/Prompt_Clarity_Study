import sys

MOD = 1000000007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    counts = [next(it) for _ in range(n)]

    k = next(it)
    restricted = {next(it) - 1 for _ in range(k)}

    length = next(it)
    sequence = [next(it) - 1 for _ in range(length)]

    blocks = 0
    if sequence:
        blocks = min(counts[color] for color in sequence)
        for color in sequence:
            counts[color] -= blocks

    restricted_total = sum(counts[color] for color in restricted)
    unrestricted_total = sum(counts) - restricted_total + blocks

    if restricted_total > unrestricted_total + 1:
        print(0)
        return

    limit = max(unrestricted_total + 1, blocks, max(counts))
    factorial = [1] * (limit + 1)
    for i in range(1, limit + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inverse_factorial = [1] * (limit + 1)
    inverse_factorial[limit] = pow(factorial[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

    answer = factorial[unrestricted_total]
    answer = answer * factorial[unrestricted_total + 1] % MOD
    answer = answer * inverse_factorial[
        unrestricted_total + 1 - restricted_total
    ] % MOD
    answer = answer * inverse_factorial[blocks] % MOD

    for count in counts:
        answer = answer * inverse_factorial[count] % MOD

    print(answer)


if __name__ == "__main__":
    main()