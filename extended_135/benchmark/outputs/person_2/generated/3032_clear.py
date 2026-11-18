import sys
from itertools import combinations
from functools import lru_cache

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    b = int(data[0])
    s = int(data[1])
    tokens = data[2:]

    ids = sorted({int(t[1:]) for t in tokens if t[0] == 86})
    n = len(ids)
    index = {v: i for i, v in enumerate(ids)}

    code = []
    repetitions = []
    multiplier = 1
    references = 0

    for token in tokens:
        kind = token[0]
        if kind == 86:
            code.append((index[int(token[1:])], multiplier, 0))
            references += multiplier
        elif kind == 82:
            count = int(token[1:])
            repetitions.append((multiplier, count))
            multiplier *= count
            code.append((-1, 0, 0))
        else:
            parent_multiplier, count = repetitions.pop()
            code.append((-2, parent_multiplier * (count - 1), parent_multiplier))
            multiplier = parent_multiplier

    if n <= s:
        print(references)
        return

    m = n - s
    limit = 1 << m
    full = limit - 1
    sizes = [0] * limit
    low_index = [0] * limit
    for mask in range(1, limit):
        bit = mask & -mask
        sizes[mask] = sizes[mask ^ bit] + 1
        low_index[mask] = bit.bit_length() - 1

    bank_count = min(b - 1, (m + 1) // 2) if s >= 2 else b - 1

    options = None
    if s >= 3:
        options = [[] for _ in range(limit)]
        for mask in range(1, limit):
            if sizes[mask] <= s:
                continue
            bit = mask & -mask
            rest = mask ^ bit
            sub = rest
            current = options[mask]
            while True:
                if sizes[sub] < s:
                    group = sub | bit
                    remaining = rest ^ sub
                    current.append((group, remaining, sizes[remaining]))
                if sub == 0:
                    break
                sub = (sub - 1) & rest

    best_extra = references + 1

    for zero_vars in combinations(range(n), s):
        mapping = [0] * n
        for v in zero_vars:
            mapping[v] = -1
        at = 0
        for v in range(n):
            if mapping[v] != -1:
                mapping[v] = at
                at += 1

        weights = [[0] * m for _ in range(m)]
        stack = []
        first = last = -1
        total_edges = 0

        for kind, x, y in code:
            if kind >= 0:
                v = mapping[kind]
                if v < 0:
                    continue
                if first < 0:
                    first = v
                if last >= 0 and last != v:
                    weights[last][v] += x
                    weights[v][last] += x
                    total_edges += x
                last = v
            elif kind == -1:
                stack.append((first, last))
                first = last = -1
            else:
                parent_first, parent_last = stack.pop()
                if first >= 0:
                    if last != first and x:
                        weights[last][first] += x
                        weights[first][last] += x
                        total_edges += x
                    if parent_last >= 0 and parent_last != first:
                        weights[parent_last][first] += y
                        weights[first][parent_last] += y
                        total_edges += y
                    if parent_first >= 0:
                        first = parent_first
                else:
                    first, last = parent_first, parent_last

        if s == 1:
            extra = total_edges + 1
        elif s == 2:
            memo = [-1] * limit
            memo[0] = 0

            def matching(mask):
                cached = memo[mask]
                if cached >= 0:
                    return cached
                i = low_index[mask]
                rest = mask & (mask - 1)
                answer = matching(rest)
                row = weights[i]
                choices = rest
                while choices:
                    bit = choices & -choices
                    j = bit.bit_length() - 1
                    value = row[j] + matching(rest ^ bit)
                    if value > answer:
                        answer = value
                    choices ^= bit
                memo[mask] = answer
                return answer

            extra = total_edges - matching(full) + 1
        else:
            internal = [0] * limit
            for mask in range(1, limit):
                rest = mask & (mask - 1)
                row = weights[low_index[mask]]
                value = internal[rest]
                bits = rest
                while bits:
                    bit = bits & -bits
                    value += row[bit.bit_length() - 1]
                    bits ^= bit
                internal[mask] = value

            @lru_cache(None)
            def partition(mask, banks):
                if sizes[mask] <= s:
                    return internal[mask]
                answer = -1
                capacity = (banks - 1) * s
                for group, remaining, count in options[mask]:
                    if count > capacity:
                        continue
                    value = internal[group] + partition(remaining, banks - 1)
                    if value > answer:
                        answer = value
                return answer

            extra = total_edges - partition(full, bank_count) + 1
            partition.cache_clear()

        if extra < best_extra:
            best_extra = extra
            if extra == 1:
                break

    print(references + best_extra)

if __name__ == "__main__":
    main()
