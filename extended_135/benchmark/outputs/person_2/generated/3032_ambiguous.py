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

    variables = sorted({int(t[1:]) for t in tokens if t[0] == 86})
    n = len(variables)
    index = {v: i for i, v in enumerate(variables)}

    total_refs = 0
    multiplier = 1
    repeats = []
    for token in tokens:
        kind = token[0]
        if kind == 86:
            total_refs += multiplier
        elif kind == 82:
            r = int(token[1:])
            repeats.append(r)
            multiplier *= r
        else:
            multiplier //= repeats.pop()

    if n <= s:
        print(total_refs)
        return
    if n <= 2 * s:
        print(total_refs + 1)
        return

    nodes = []
    stack = []
    current = -1

    for token in tokens:
        kind = token[0]
        if kind == 86:
            node = len(nodes)
            nodes.append((0, index[int(token[1:])], 0))
            if current < 0:
                current = node
            else:
                nodes.append((1, current, node))
                current = len(nodes) - 1
        elif kind == 82:
            stack.append((current, int(token[1:])))
            current = -1
        else:
            parent, count = stack.pop()
            if count != 1:
                nodes.append((2, current, count))
                current = len(nodes) - 1
            if parent >= 0:
                nodes.append((1, parent, current))
                current = len(nodes) - 1

    size = len(nodes)
    multiplicities = [0] * size
    multiplicities[current] = 1
    for i in range(size - 1, -1, -1):
        typ, x, y = nodes[i]
        mult = multiplicities[i]
        if typ == 1:
            multiplicities[x] = mult
            multiplicities[y] = mult
        elif typ == 2:
            multiplicities[x] = mult * y

    operations = []
    for i, (typ, x, y) in enumerate(nodes):
        weight = multiplicities[i]
        if typ == 2:
            weight *= y - 1
        operations.append((typ, x, y, weight))

    m = n - s
    limit = 1 << m
    full = limit - 1
    popcount = [0] * limit
    low_index = [0] * limit
    for mask in range(1, limit):
        bit = mask & -mask
        popcount[mask] = popcount[mask ^ bit] + 1
        low_index[mask] = bit.bit_length() - 1

    group_options = None
    if s > 1:
        group_options = [[] for _ in range(limit)]
        for mask in range(1, limit):
            if popcount[mask] <= s:
                continue
            bit = mask & -mask
            rest = mask ^ bit
            sub = rest
            options = group_options[mask]
            while True:
                if popcount[sub] < s:
                    options.append(sub | bit)
                if sub == 0:
                    break
                sub = (sub - 1) & rest

    best_changes = total_refs + 1
    all_variables = (1 << n) - 1

    for zero_variables in combinations(range(n), s):
        zero_mask = 0
        for v in zero_variables:
            zero_mask |= 1 << v

        graph = [[0] * n for _ in range(n)]
        first = [-1] * size
        last = [-1] * size

        for i, (typ, x, y, weight) in enumerate(operations):
            if typ == 0:
                if not (zero_mask >> x) & 1:
                    first[i] = x
                    last[i] = x
            elif typ == 1:
                fx = first[x]
                fy = first[y]
                lx = last[x]
                ly = last[y]
                first[i] = fx if fx >= 0 else fy
                last[i] = ly if ly >= 0 else lx
                if lx >= 0 and fy >= 0 and lx != fy:
                    graph[lx][fy] += weight
                    graph[fy][lx] += weight
            else:
                f = first[x]
                l = last[x]
                first[i] = f
                last[i] = l
                if f >= 0 and f != l:
                    graph[f][l] += weight
                    graph[l][f] += weight

        remaining = all_variables ^ zero_mask
        vertices = []
        while remaining:
            bit = remaining & -remaining
            vertices.append(bit.bit_length() - 1)
            remaining ^= bit

        local = [[graph[u][v] for v in vertices] for u in vertices]
        total_weight = sum(map(sum, local)) // 2

        if s == 1:
            changes = total_weight + 1
        else:
            scores = [0] * limit
            for mask in range(1, limit):
                bit = mask & -mask
                i = low_index[mask]
                rest = mask ^ bit
                value = scores[rest]
                row = local[i]
                scan = rest
                while scan:
                    other = scan & -scan
                    value += row[other.bit_length() - 1]
                    scan ^= other
                scores[mask] = value

            @lru_cache(None)
            def solve(mask, banks):
                count = popcount[mask]
                if count <= s:
                    return scores[mask]
                if banks <= 1:
                    return -10**18

                answer = -10**18
                capacity = (banks - 1) * s
                for group in group_options[mask]:
                    rest = mask ^ group
                    if popcount[rest] > capacity:
                        continue
                    value = scores[group] + solve(
                        rest, min(banks - 1, popcount[rest])
                    )
                    if value > answer:
                        answer = value
                        if answer == scores[mask]:
                            break
                return answer

            saved = solve(full, min(b - 1, m))
            changes = total_weight - saved + 1
            solve.cache_clear()

        if changes < best_changes:
            best_changes = changes
            if best_changes == 1:
                break

    print(total_refs + best_changes)


if __name__ == "__main__":
    main()
