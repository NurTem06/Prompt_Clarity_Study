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

        for j, value in enumerate(b_poly):
            c[j + shift] = (c[j + shift] - factor * value) % MOD

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
    if not size:
        return 0

    nonzero = [(j, value) for j, value in enumerate(recurrence) if value]

    def multiply(a, b):
        result = [0] * (2 * size - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        result[i + j] += x * y

        for i in range(2 * size - 2, size - 1, -1):
            value = result[i] % MOD
            if value:
                for j, coefficient in nonzero:
                    result[i - 1 - j] += value * coefficient

        return [value % MOD for value in result[:size]]

    answer = [0] * size
    answer[0] = 1
    base = [0] * size
    if size == 1:
        base[0] = recurrence[0]
    else:
        base[1] = 1

    while index:
        if index & 1:
            answer = multiply(answer, base)
        index >>= 1
        if index:
            base = multiply(base, base)

    return sum(x * y for x, y in zip(answer, initial)) % MOD


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    counts = data[:4]
    n = data[4]
    total = sum(counts)

    if n == 1:
        print(total * (total - 1) % MOD)
        return
    if total < 2:
        print(0)
        return

    states = []
    state_ids = {}
    initial_weights = []

    def get_state(state):
        existing = state_ids.get(state)
        if existing is not None:
            return existing
        index = len(states)
        state_ids[state] = index
        states.append(state)
        initial_weights.append(0)
        return index

    for a in range(4):
        if not counts[a]:
            continue
        for b in range(4):
            ways = counts[a] * (counts[b] - (a == b))
            if ways:
                index = get_state((a, b, 0, -1))
                initial_weights[index] = ways

    edges = []
    pos = 0
    while pos < len(states):
        a, b, streak, rest = states[pos]
        successful = a // 2 != b % 2
        outgoing = []

        if successful and streak == 2:
            available = counts[:]
            available[a] -= 1
            available[b] -= 1
            for c in range(4):
                if available[c] <= 0:
                    continue
                for d in range(4):
                    ways = available[c] * (available[d] - (c == d))
                    if ways > 0:
                        target = get_state((c, d, 0, a))
                        outgoing.append((target, ways))
        else:
            next_rest = rest + 4 if 0 <= rest < 4 else -1
            next_attacker = a if successful else b
            next_streak = streak + 1 if successful else 0

            available = counts[:]
            available[a] -= 1
            available[b] -= 1
            if 0 <= rest < 4:
                available[rest] -= 1

            for c in range(4):
                if available[c] > 0:
                    target = get_state(
                        (next_attacker, c, next_streak, next_rest)
                    )
                    outgoing.append((target, available[c]))

        edges.append(outgoing)
        pos += 1

    dimension = len(states)
    terms_needed = min(n, 2 * dimension + 2)
    vector = initial_weights
    sequence = []

    for step in range(terms_needed):
        sequence.append(sum(vector) % MOD)
        if step + 1 == terms_needed:
            break
        next_vector = [0] * dimension
        for i, value in enumerate(vector):
            if value:
                for target, weight in edges[i]:
                    next_vector[target] += value * weight
        vector = [value % MOD for value in next_vector]

    if n <= len(sequence):
        print(sequence[n - 1])
        return

    recurrence = berlekamp_massey(sequence)
    print(recurrence_term(sequence, recurrence, n - 1))


if __name__ == "__main__":
    main()
