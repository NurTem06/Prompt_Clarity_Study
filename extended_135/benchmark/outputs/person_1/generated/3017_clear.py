import sys


def main():
    n, e = map(int, sys.stdin.buffer.read().split())
    pattern = str(1 << e)
    digits = str(n)
    m = len(pattern)

    if m > len(digits):
        print(0)
        return

    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    unstarted = m + 1
    transitions = [[0] * 10 for _ in range(m + 2)]

    for state in range(m):
        for digit in range(10):
            char = str(digit)
            j = state
            while j and pattern[j] != char:
                j = pi[j - 1]
            if pattern[j] == char:
                j += 1
            transitions[state][digit] = j

    transitions[m] = [m] * 10
    transitions[unstarted][0] = unstarted
    for digit in range(1, 10):
        transitions[unstarted][digit] = transitions[0][digit]

    loose = [0] * (m + 2)
    tight = [0] * (m + 2)
    tight[unstarted] = 1

    for char in digits:
        limit = int(char)
        next_loose = [0] * (m + 2)
        next_tight = [0] * (m + 2)

        for state in range(m + 2):
            row = transitions[state]
            count = loose[state]
            if count:
                for destination in row:
                    next_loose[destination] += count

            count = tight[state]
            if count:
                for digit in range(limit):
                    next_loose[row[digit]] += count
                next_tight[row[limit]] += count

        loose, tight = next_loose, next_tight

    print(loose[m] + tight[m])


if __name__ == "__main__":
    main()
