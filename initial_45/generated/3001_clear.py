import sys


def main():
    s = sys.stdin.buffer.read().strip()
    if not s:
        return

    digits = [c - 48 for c in s]
    n = len(digits)
    inf = 10**9

    # State: outgoing carry on the left, incoming carry on the right.
    dp = [[0, inf], [0, inf]]

    for i in range(n // 2):
        a = digits[i]
        b = digits[n - 1 - i]
        nxt = [[inf, inf], [inf, inf]]

        for left_out in range(2):
            for right_in in range(2):
                current = dp[left_out][right_in]
                if current == inf:
                    continue

                for target in range(10):
                    right_steps = (target - b - right_in) % 10
                    right_out = (b + right_in + right_steps) // 10

                    for left_in in range(2):
                        left_steps = target - a - left_in + 10 * left_out
                        if 0 <= left_steps <= 9:
                            cost = current + left_steps + right_steps
                            if cost < nxt[left_in][right_out]:
                                nxt[left_in][right_out] = cost

        dp = nxt

    if n % 2 == 0:
        answer = min(dp[0][0], dp[1][1])
    else:
        answer = inf
        middle = digits[n // 2]
        for left_out in range(2):
            for right_in in range(2):
                for steps in range(10):
                    if (middle + right_in + steps) // 10 == left_out:
                        answer = min(answer, dp[left_out][right_in] + steps)

    print(answer)


if __name__ == "__main__":
    main()
