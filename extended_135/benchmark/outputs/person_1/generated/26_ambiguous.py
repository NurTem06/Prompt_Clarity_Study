import sys
from decimal import Decimal, localcontext

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    with localcontext() as ctx:
        ctx.prec = 80
        values = [Decimal(s.decode()) for s in data]
        logs = [v.ln() for v in values]
        names = "xyz"
        tolerance = Decimal("1e-65")

        best_sign = -2
        best_score = Decimal(0)
        answer = ""

        for i in range(3):
            j, k = [t for t in range(3) if t != i]
            a, b, c = names[i], names[j], names[k]

            expressions = [
                f"{a}^{b}^{c}",
                f"{a}^{c}^{b}",
                f"({a}^{b})^{c}",
                f"({a}^{c})^{b}",
            ]

            sign = (logs[i] > 0) - (logs[i] < 0)

            if sign == 0:
                scores = [Decimal(0)] * 4
            else:
                base_score = abs(logs[i]).ln()
                scores = [
                    base_score + values[k] * logs[j],
                    base_score + values[j] * logs[k],
                    base_score + (logs[j] + logs[k]),
                    base_score + (logs[j] + logs[k]),
                ]

            for expression, score in zip(expressions, scores):
                ranked_score = score * sign
                if (sign > best_sign or
                    (sign == best_sign and
                     ranked_score - best_score > tolerance)):
                    best_sign = sign
                    best_score = ranked_score
                    answer = expression

        print(answer)

if __name__ == "__main__":
    main()