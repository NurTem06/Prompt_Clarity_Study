import sys

MOD = 1_000_000_007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    counts = data[1:n + 1]
    pos = n + 1

    k = data[pos]
    pos += 1
    forbidden = {x - 1 for x in data[pos:pos + k]}
    pos += k

    length = data[pos]
    pos += 1
    sequence = [x - 1 for x in data[pos:pos + length]]

    blocks = 0
    if sequence:
        blocks = min(counts[color] for color in sequence)
        for color in sequence:
            counts[color] -= blocks

    forbidden_total = sum(counts[color] for color in forbidden)
    allowed_total = sum(counts) - forbidden_total + blocks

    if forbidden_total > allowed_total + 1:
        print(0)
        return

    limit = max(sum(counts) + blocks + 1, max(counts), blocks)
    factorial = [1] * (limit + 1)
    for i in range(1, limit + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inverse_factorial = [1] * (limit + 1)
    inverse_factorial[limit] = pow(factorial[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

    answer = factorial[allowed_total]
    answer = answer * factorial[allowed_total + 1] % MOD
    answer = answer * inverse_factorial[allowed_total + 1 - forbidden_total] % MOD
    answer = answer * inverse_factorial[blocks] % MOD

    for count in counts:
        answer = answer * inverse_factorial[count] % MOD

    print(answer)


if __name__ == "__main__":
    main()
