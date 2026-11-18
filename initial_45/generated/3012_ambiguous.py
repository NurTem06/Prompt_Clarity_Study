import sys

MOD = 1000000007


def berlekamp_massey(sequence):
    c = [1]
    b_poly = [1]
    length = 0
    shift = 1
    last = 1

    for n in range(len(sequence)):
        discrepancy = sequence[n]
        for i in range(1, length + 1):
            discrepancy += c[i] * sequence[n - i]
        discrepancy %= MOD

        if discrepancy == 0:
            shift += 1
            continue

        old_c = c[:]
        factor = discrepancy * pow(last, MOD - 2, MOD) % MOD
        needed = len(b_poly) + shift
        if len(c) < needed:
            c.extend([0] * (needed - len(c)))
        for i, value in enumerate(b_poly):
            c[i + shift] = (c[i + shift] - factor * value) % MOD

        if 2 * length <= n:
            length = n + 1 - length
            b_poly = old_c
            last = discrepancy
            shift = 1
        else:
            shift += 1

    return [(-c[i]) % MOD for i in range(1, length + 1)]


def recurrence_term(initial, recurrence, index):
    size = len(recurrence)
    if size == 0:
        return 0

    def multiply(a, b):
        product = [0] * (2 * size - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        product[i + j] += x * y
        for i in range(len(product)):
            product[i] %= MOD

        for i in range(2 * size - 2, size - 1, -1):
            value = product[i]
            if value:
                for j, coefficient in enumerate(recurrence, 1):
                    product[i - j] = (
                        product[i - j] + value * coefficient
                    ) % MOD
        return product[:size]

    result = [0] * size
    result[0] = 1
    base = [0] * size
    if size == 1:
        base[0] = recurrence[0]
    else:
        base[1] = 1

    while index:
        if index & 1:
            result = multiply(result, base)
        index >>= 1
        if index:
            base = multiply(base, base)

    return sum(x * y for x, y in zip(result, initial)) % MOD


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    counts = data[:4]
    n = data[4]
    total = sum(counts)

    if total < 2:
        print(0)
        return
    if n == 1:
        print(total * (total - 1) % MOD)
        return

    pairs = [
        (i, j)
        for i in range(4)
        for j in range(4)
        if counts[i] > 0 and counts[j] - (i == j) > 0
    ]
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    pair_count = len(pairs)
    state_count = pair_count * 3
    transitions = [[] for _ in range(state_count)]

    vector = [0] * state_count
    for p, (i, j) in enumerate(pairs):
        vector[p] = counts[i] * (counts[j] - (i == j)) % MOD
        remaining = [
            counts[k] - (k == i) - (k == j)
            for k in range(4)
        ]
        defense_wins = i // 2 == j % 2

        for streak in range(3):
            edges = transitions[streak * pair_count + p]
            if defense_wins:
                for k in range(4):
                    if remaining[k] > 0:
                        edges.append((pair_index[(j, k)], remaining[k]))
            elif streak < 2:
                offset = (streak + 1) * pair_count
                for k in range(4):
                    if remaining[k] > 0:
                        edges.append(
                            (offset + pair_index[(i, k)], remaining[k])
                        )
            else:
                for k in range(4):
                    if remaining[k] <= 0:
                        continue
                    for l in range(4):
                        ways = remaining[l] - (k == l)
                        if ways > 0:
                            edges.append(
                                (pair_index[(k, l)], remaining[k] * ways)
                            )

    target = n - 1
    terms_needed = min(n, 2 * state_count + 1)
    sequence = []

    for step in range(terms_needed):
        sequence.append(sum(vector) % MOD)
        if step == target:
            print(sequence[-1])
            return

        next_vector = [0] * state_count
        for source, value in enumerate(vector):
            if value:
                for destination, ways in transitions[source]:
                    next_vector[destination] += value * ways
        vector = [value % MOD for value in next_vector]

    recurrence = berlekamp_massey(sequence)
    print(recurrence_term(sequence, recurrence, target))


if __name__ == "__main__":
    main()