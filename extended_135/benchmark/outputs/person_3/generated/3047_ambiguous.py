import sys
import math
from itertools import product


def divisors(n):
    result = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
    return result


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    plates = [
        [tokens[2 * i], tokens[2 * i + 1],
         tokens[10 + 2 * i], tokens[11 + 2 * i]]
        for i in range(5)
    ]

    column_gcds = [0] * 4
    constraints = []

    for plate in plates:
        known = []
        for j, token in enumerate(plate):
            if token != b'_':
                value = int(token)
                column_gcds[j] = math.gcd(column_gcds[j], value)
                known.append((j, value))

        if not known:
            print("many")
            return

        first_j, first_value = known[0]
        for j, value in known[1:]:
            constraints.append((first_j, j, first_value, value))

    if 0 in column_gcds:
        print("many")
        return

    answer = 0
    choices = [divisors(g) for g in column_gcds]

    for values in product(*choices):
        if math.gcd(*values) != 1:
            continue

        if all(a * values[j] == b * values[i]
               for i, j, a, b in constraints):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
