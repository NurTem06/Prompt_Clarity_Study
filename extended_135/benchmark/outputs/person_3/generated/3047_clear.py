import sys
from math import gcd, isqrt
from itertools import product


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    plates = [[] for _ in range(5)]
    column_gcd = [0] * 4

    for index, token in enumerate(tokens):
        if token == b'_':
            continue
        monster = (index % 10) // 2
        food = (index // 10) * 2 + index % 2
        value = int(token)
        plates[monster].append((food, value))
        column_gcd[food] = gcd(column_gcd[food], value)

    if any(not plate for plate in plates) or any(x == 0 for x in column_gcd):
        print("many")
        return

    def divisors(n):
        result = []
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                result.append(d)
                if d * d != n:
                    result.append(n // d)
        return result

    constraints = []
    for plate in plates:
        first_food, first_value = plate[0]
        for food, value in plate[1:]:
            constraints.append((first_food, first_value, food, value))

    answer = 0
    for vector in product(*(divisors(n) for n in column_gcd)):
        if gcd(gcd(vector[0], vector[1]), gcd(vector[2], vector[3])) != 1:
            continue
        for first_food, first_value, food, value in constraints:
            if first_value * vector[food] != value * vector[first_food]:
                break
        else:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
