import sys
from math import comb

MOD = 1_000_000_007


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    m = len(s)
    length = 2 * n

    if m > length or s.count(b'(') > n or s.count(b')') > n:
        print(0)
        return

    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    transitions = []
    for char in (40, 41):
        trans = [0] * m
        for k in range(m):
            if s[k] == char:
                trans[k] = k + 1
            elif k:
                trans[k] = trans[pi[k - 1]]
        transitions.append(trans)

    opening, closing = transitions
    size = (n + 1) * m
    dp = [0] * size
    dp[0] = 1

    for pos in range(length):
        nxt = [0] * size
        max_balance = min(pos, length - pos, n)
        next_limit = min(length - pos - 1, n)
        state_limit = min(pos + 1, m)

        for balance in range(pos & 1, max_balance + 1, 2):
            base = balance * m
            can_open = balance < next_limit
            can_close = balance > 0
            for k in range(state_limit):
                value = dp[base + k]
                if not value:
                    continue

                if can_open:
                    state = opening[k]
                    if state < m:
                        index = base + m + state
                        result = nxt[index] + value
                        nxt[index] = result - MOD if result >= MOD else result

                if can_close:
                    state = closing[k]
                    if state < m:
                        index = base - m + state
                        result = nxt[index] + value
                        nxt[index] = result - MOD if result >= MOD else result

        dp = nxt

    avoiding = sum(dp[:m]) % MOD
    total = comb(length, n) // (n + 1)
    print((total - avoiding) % MOD)


if __name__ == "__main__":
    main()
