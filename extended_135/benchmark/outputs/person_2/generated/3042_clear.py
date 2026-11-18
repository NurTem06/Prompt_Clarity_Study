import sys
from math import gcd, comb
from functools import lru_cache

MOD = 1000000007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = sorted(data[1:1 + n])
    if n == 1:
        print(1)
        return

    values = []
    multiplicities = []
    for x in arr:
        if values and values[-1] == x:
            multiplicities[-1] += 1
        else:
            values.append(x)
            multiplicities.append(1)

    m = len(values)
    if any(values[-1] % x for x in values):
        print(0)
        return

    starts = []
    groups = []
    prefixes = []
    bit_type = []
    pos = 0
    for t, c in enumerate(multiplicities):
        starts.append(pos)
        groups.append(((1 << c) - 1) << pos)
        prefixes.append([((1 << k) - 1) << pos for k in range(c + 1)])
        bit_type.extend([t] * c)
        pos += c

    divides = [[False] * m for _ in range(m)]
    divisor_masks = [0] * m
    for i in range(m):
        for j in range(i + 1):
            if values[i] % values[j] == 0:
                divides[i][j] = True
                divisor_masks[i] |= groups[j]

    pairs = [[] for _ in range(m)]
    proper_pairs = [[] for _ in range(m)]
    for r in range(m):
        v = values[r]
        for i in range(r + 1):
            if not divides[r][i]:
                continue
            for j in range(i + 1, r + 1):
                if divides[r][j] and values[i] // gcd(values[i], values[j]) * values[j] == v:
                    pairs[r].append((i, j, divisor_masks[i] | divisor_masks[j]))
                    if j < r:
                        proper_pairs[r].append((i, j))
        pairs[r].append((r, r, divisor_masks[r]))

    uniform = [0] * (n + 1)
    uniform[1] = 1
    for size in range(3, n + 1, 2):
        total = 0
        for left in range(1, size - 1, 2):
            total += comb(size - 1, left) * uniform[left] * uniform[size - 1 - left]
        uniform[size] = (total % MOD) * size * ((MOD + 1) // 2) % MOD

    @lru_cache(maxsize=None)
    def solve(mask):
        size = mask.bit_count()
        if size == 1:
            return 1
        if not size & 1:
            return 0

        r = bit_type[mask.bit_length() - 1]
        if mask & ~divisor_masks[r]:
            return 0

        root_count = (mask & groups[r]).bit_count()
        if mask & ~groups[r] == 0:
            return uniform[size]

        remaining = mask ^ (1 << (mask.bit_length() - 1))
        counts = [0] * (r + 1)
        active = []
        for t in range(r + 1):
            c = (remaining & groups[t]).bit_count()
            if c:
                counts[t] = c
                active.append(t)

        leaf_only = [False] * (r + 1)
        for t in active:
            if counts[t] == 1:
                leaf_only[t] = not any(
                    counts[a] and counts[b]
                    for a, b in proper_pairs[t]
                )

        answer = 0
        for i, j, cover in pairs[r]:
            if not counts[i] or not counts[j]:
                continue
            if i == j and counts[i] < 2:
                continue
            if remaining & ~cover:
                continue

            if i != j and leaf_only[i]:
                a = prefixes[i][1]
                b = remaining ^ a
                if bit_type[b.bit_length() - 1] == j:
                    answer += solve(b)
                continue
            if i != j and leaf_only[j]:
                b = prefixes[j][1]
                a = remaining ^ b
                if bit_type[a.bit_length() - 1] == i:
                    answer += solve(a)
                continue
            if i == j and counts[i] == 2 and not any(
                counts[a] and counts[b] for a, b in proper_pairs[i]
            ):
                if size == 3:
                    answer += 1
                continue

            forced_a = 0
            forced_b = 0
            options = []
            valid = True

            for t in active:
                c = counts[t]
                da = divides[i][t]
                db = divides[j][t]
                if not db:
                    forced_a |= prefixes[t][c]
                elif not da:
                    forced_b |= prefixes[t][c]
                else:
                    low = 1 if t == i else 0
                    high = c - 1 if t == j else c
                    if low > high:
                        valid = False
                        break
                    pref = prefixes[t]
                    if i == j and t == i:
                        opts = [
                            (pref[k], pref[c - k], comb(c - 1, k - 1))
                            for k in range(low, high + 1)
                        ]
                    else:
                        opts = [
                            (pref[k], pref[c - k], comb(c, k))
                            for k in range(low, high + 1)
                        ]
                    if len(opts) == 1:
                        aa, bb, _ = opts[0]
                        forced_a |= aa
                        forced_b |= bb
                    else:
                        options.append(opts)

            if not valid:
                continue

            length = len(options)

            def enumerate_splits(index, a, b, weight):
                if index == length:
                    if not a or not b or not (a.bit_count() & 1):
                        return 0
                    if a.bit_count() <= b.bit_count():
                        first = solve(a)
                        if not first:
                            return 0
                        second = solve(b)
                    else:
                        second = solve(b)
                        if not second:
                            return 0
                        first = solve(a)
                    return weight * first % MOD * second % MOD

                total = 0
                for aa, bb, factor in options[index]:
                    total += enumerate_splits(
                        index + 1, a | aa, b | bb, weight * factor % MOD
                    )
                return total % MOD

            answer += enumerate_splits(0, forced_a, forced_b, 1)
            answer %= MOD

        return answer * root_count % MOD

    print(solve((1 << n) - 1))


if __name__ == "__main__":
    main()
