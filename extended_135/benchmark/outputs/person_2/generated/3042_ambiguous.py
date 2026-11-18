import sys
import math
from functools import lru_cache

MOD = 1000000007
INV2 = (MOD + 1) // 2


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    values_input = data[1:1 + n]

    if n == 1:
        print(1)
        return

    values = sorted(set(values_input))
    k = len(values)
    index = {v: i for i, v in enumerate(values)}
    limits = [0] * k
    for v in values_input:
        limits[index[v]] += 1

    top = values[-1]
    if any(top % v for v in values):
        print(0)
        return

    bases = [c + 1 for c in limits]
    units = [1] * k
    for i in range(1, k):
        units[i] = units[i - 1] * bases[i - 1]

    full_state = sum(c * u for c, u in zip(limits, units))

    choose = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        choose[i][0] = choose[i][i] = 1
        for j in range(1, i):
            choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j]

    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    same_value_answer = [0] * (n + 1)
    for s in range(1, n + 1, 2):
        m = s // 2
        catalan = math.comb(2 * m, m) // (m + 1)
        same_value_answer[s] = (
            factorial[s] * (catalan % MOD) % MOD
            * pow(INV2, m, MOD) % MOD
        )

    divides = [[False] * k for _ in range(k)]
    divisor_masks = [0] * k
    for i, v in enumerate(values):
        mask = 0
        for j in range(i + 1):
            if v % values[j] == 0:
                divides[i][j] = True
                mask |= 1 << j
        divisor_masks[i] = mask

    pairs = [[] for _ in range(k)]
    proper_pairs = [[] for _ in range(k)]
    for a in range(k):
        for b in range(a, k):
            lcm = values[a] // math.gcd(values[a], values[b]) * values[b]
            r = index.get(lcm)
            if r is not None:
                pairs[r].append((a, b))
                if b < r:
                    proper_pairs[r].append((a, b))

    @lru_cache(maxsize=None)
    def solve(state):
        counts = [0] * k
        present = []
        mask = 0
        size = 0
        x = state
        for i in range(k):
            c = x % bases[i]
            x //= bases[i]
            if c:
                counts[i] = c
                present.append(i)
                mask |= 1 << i
                size += c
            if not x:
                break

        if not (size & 1):
            return 0
        if len(present) == 1:
            return same_value_answer[size]

        root = present[-1]
        if mask & ~divisor_masks[root]:
            return 0

        needed = size // 2
        capacity = 0
        for i in present:
            c = counts[i]
            lower = 0
            for j in present:
                if j >= i:
                    break
                if divides[i][j]:
                    lower += counts[j]

            bound = min(c, (c - 1 + lower) // 2)
            if not bound:
                continue

            possible = c >= 3 or (c >= 2 and lower > 0)
            if not possible:
                for a, b in proper_pairs[i]:
                    if counts[a] and counts[b] and (a != b or counts[a] >= 2):
                        possible = True
                        break
            if possible:
                capacity += bound

        if capacity < needed:
            return 0

        root_choices = counts[root]
        counts[root] -= 1
        remaining_state = state - units[root]
        remaining_present = [i for i in present if counts[i]]
        remaining_mask = mask
        if counts[root] == 0:
            remaining_mask ^= 1 << root

        answer = 0

        for a, b in pairs[root]:
            if not counts[a] or not counts[b]:
                continue
            if a == b and counts[a] < 2:
                continue
            if remaining_mask & ~(divisor_masks[a] | divisor_masks[b]):
                continue

            left_code = 0
            left_size = 0
            weight = 1
            options = []
            valid = True

            for i in remaining_present:
                c = counts[i]
                in_a = divides[a][i]
                in_b = divides[b][i]

                if not in_b:
                    left_code += c * units[i]
                    left_size += c
                elif not in_a:
                    pass
                else:
                    low = 1 if i == a else 0
                    high = c - 1 if i == b else c
                    if low > high:
                        valid = False
                        break
                    if low == high:
                        left_code += low * units[i]
                        left_size += low
                        weight = weight * choose[c][low] % MOD
                    else:
                        opts = [
                            (t * units[i], t, choose[c][t])
                            for t in range(low, high + 1)
                        ]
                        options.append(opts)

            if not valid:
                continue

            symmetric = a == b
            half = remaining_state // 2
            if symmetric and left_code > half:
                continue

            options.reverse()
            option_count = len(options)

            def enumerate_splits(pos, code, count, ways):
                if symmetric and code > half:
                    return 0
                if pos == option_count:
                    if not (count & 1):
                        return 0
                    first = solve(code)
                    if not first:
                        return 0
                    other_code = remaining_state - code
                    second = solve(other_code)
                    if not second:
                        return 0
                    result = ways * first % MOD * second % MOD
                    if symmetric and code == other_code:
                        result = result * INV2 % MOD
                    return result

                result = 0
                last = pos + 1 == option_count
                for increment, amount, multiplicity in options[pos]:
                    if last and not ((count + amount) & 1):
                        continue
                    result += enumerate_splits(
                        pos + 1,
                        code + increment,
                        count + amount,
                        ways * multiplicity % MOD,
                    )
                return result % MOD

            answer += enumerate_splits(0, left_code, left_size, weight)
            answer %= MOD

        return answer * root_choices % MOD

    print(solve(full_state))


if __name__ == "__main__":
    main()
