import sys


def main():
    s = sys.stdin.buffer.readline().strip()
    if not s:
        return

    digits = [c - 48 for c in s]
    n = len(digits)
    inf = 10**9

    # State: carry leaving the left boundary, carry entering the right boundary.
    dp = [0, inf, 0, inf]

    for i in range(n // 2):
        a = digits[i]
        b = digits[n - 1 - i]
        ndp = [inf] * 4

        for state, cost in enumerate(dp):
            if cost == inf:
                continue

            left_out = state >> 1
            right_in = state & 1

            for digit in range(10):
                for left_in in range(2):
                    left_cost = digit + 10 * left_out - a - left_in
                    if not 0 <= left_cost <= 9:
                        continue

                    for right_out in range(2):
                        right_cost = digit + 10 * right_out - b - right_in
                        if 0 <= right_cost <= 9:
                            new_state = (left_in << 1) | right_out
                            value = cost + left_cost + right_cost
                            if value < ndp[new_state]:
                                ndp[new_state] = value

        dp = ndp

    if n % 2 == 0:
        answer = min(dp[0], dp[3])
    else:
        answer = inf
        a = digits[n // 2]
        for state, cost in enumerate(dp):
            if cost == inf:
                continue
            carry_out = state >> 1
            carry_in = state & 1
            for digit in range(10):
                advances = digit + 10 * carry_out - a - carry_in
                if 0 <= advances <= 9:
                    answer = min(answer, cost + advances)

    print(answer)


if __name__ == "__main__":
    main()
