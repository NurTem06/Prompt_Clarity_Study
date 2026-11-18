import sys


def main():
    n, e = map(int, sys.stdin.buffer.read().split())
    digits = str(n)
    pattern = str(1 << e)
    m = len(pattern)

    if m > len(digits):
        print(0)
        return

    prefix = [0] * m
    for i in range(1, m):
        j = prefix[i - 1]
        while j and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    transitions = [[0] * 10 for _ in range(m + 1)]
    for state in range(m):
        for digit in range(10):
            ch = str(digit)
            j = state
            while j and pattern[j] != ch:
                j = prefix[j - 1]
            if pattern[j] == ch:
                j += 1
            transitions[state][digit] = j
    transitions[m] = [m] * 10

    # Leading zero padding cannot introduce a match because the pattern
    # always starts with a nonzero digit.
    dp = [[0] * (m + 1) for _ in range(2)]
    dp[1][0] = 1

    for ch in digits:
        bound = int(ch)
        next_dp = [[0] * (m + 1) for _ in range(2)]
        for tight in range(2):
            limit = bound if tight else 9
            for state, count in enumerate(dp[tight]):
                if count:
                    for digit in range(limit + 1):
                        next_tight = int(tight and digit == bound)
                        next_state = transitions[state][digit]
                        next_dp[next_tight][next_state] += count
        dp = next_dp

    print(dp[0][m] + dp[1][m])


if __name__ == "__main__":
    main()