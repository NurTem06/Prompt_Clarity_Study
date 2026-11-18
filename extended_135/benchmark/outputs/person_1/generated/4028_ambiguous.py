import sys
from math import comb

MOD = 1000000007


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    m = len(s)
    total_length = 2 * n

    if m > total_length or s.count(b'(') > n or s.count(b')') > n:
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

    opening = [0] * m
    closing = [0] * m
    for state in range(m):
        for char, transition in ((40, opening), (41, closing)):
            if s[state] == char:
                transition[state] = state + 1
            elif state:
                transition[state] = transition[pi[state - 1]]

    dp = [[0] * m for _ in range(n + 1)]
    dp[0][0] = 1

    for pos in range(total_length):
        remaining = total_length - pos - 1
        new_dp = [[0] * m for _ in range(n + 1)]
        max_balance = min(pos, n, total_length - pos)
        state_limit = min(m, pos + 1)

        for balance in range(pos & 1, max_balance + 1, 2):
            row = dp[balance]
            up = new_dp[balance + 1] if balance < n and balance + 1 <= remaining else None
            down = new_dp[balance - 1] if balance > 0 else None

            for state in range(state_limit):
                value = row[state]
                if not value:
                    continue

                if up is not None:
                    nxt = opening[state]
                    if nxt < m:
                        result = up[nxt] + value
                        up[nxt] = result - MOD if result >= MOD else result

                if down is not None:
                    nxt = closing[state]
                    if nxt < m:
                        result = down[nxt] + value
                        down[nxt] = result - MOD if result >= MOD else result

        dp = new_dp

    catalan = comb(total_length, n) // (n + 1)
    print((catalan - sum(dp[0])) % MOD)


if __name__ == "__main__":
    main()