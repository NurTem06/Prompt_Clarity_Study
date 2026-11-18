import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    m = len(s)

    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    transitions = [[] for _ in range(m)]
    for state in range(m):
        for bit in (48, 49):
            j = state
            while j and s[j] != bit:
                j = pi[j - 1]
            if s[j] == bit:
                j += 1
            if j < m:
                transitions[state].append(j)

    avoiding = 0
    for start in range(m):
        dp = [0] * m
        dp[start] = 1
        for _ in range(n):
            nxt = [0] * m
            for state, count in enumerate(dp):
                if count:
                    for target in transitions[state]:
                        nxt[target] += count
            dp = nxt
        avoiding += dp[start]

    print((1 << n) - avoiding)


if __name__ == "__main__":
    main()