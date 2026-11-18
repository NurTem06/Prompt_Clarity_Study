import sys
import math


def main():
    values = list(map(float, sys.stdin.buffer.read().split()))
    if len(values) != 3:
        return

    names = "xyz"
    logs = [math.log(v) for v in values]
    best_sign = -2
    best_score = 0.0
    answer = ""

    for a, b, c in ((0, 1, 2), (1, 0, 2), (2, 0, 1)):
        sign = (values[a] > 1.0) - (values[a] < 1.0)
        magnitude = math.log(abs(logs[a])) if sign else 0.0

        candidates = [
            (f"{names[a]}^{names[b]}^{names[c]}",
             values[c] * logs[b]),
            (f"{names[a]}^{names[c]}^{names[b]}",
             values[b] * logs[c]),
            (f"({names[a]}^{names[b]})^{names[c]}",
             logs[b] + logs[c]),
            (f"({names[a]}^{names[c]})^{names[b]}",
             logs[b] + logs[c]),
        ]

        for expression, exponent_log in candidates:
            score = sign * (magnitude + exponent_log) if sign else 0.0
            if sign > best_sign or (
                sign == best_sign and score > best_score + 1e-12
            ):
                best_sign = sign
                best_score = score
                answer = expression

    print(answer)


if __name__ == "__main__":
    main()