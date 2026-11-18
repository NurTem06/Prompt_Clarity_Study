import sys


def main():
    s = sys.stdin.buffer.read().strip().decode()
    if not s or len(s) % 2 == 0:
        print(-1)
        return

    digits = [int(c) for c in reversed(s)]
    size = (len(digits) + 1) // 2

    if any(digits[i] % 2 for i in range(1, len(digits), 2)):
        print(-1)
        return

    parity = [digits[2 * i] % 2 for i in range(size)]
    coefficients = [d % 5 for d in digits]
    nonzero = [i for i, value in enumerate(coefficients) if value]

    root = [0] * size

    if nonzero:
        low, high = nonzero[0], nonzero[-1]
        if low % 2 or high % 2:
            print(-1)
            return

        target = coefficients[low:high + 1]
        first = next((x for x in range(1, 5)
                      if x * x % 5 == target[0]), None)
        if first is None:
            print(-1)
            return

        degree = (high - low) // 2
        part = [first] + [0] * degree
        inverse = pow(2 * first, -1, 5)

        for k in range(1, degree + 1):
            cross = sum(part[i] * part[k - i] for i in range(1, k))
            part[k] = (target[k] - cross) * inverse % 5

        square = [0] * (2 * degree + 1)
        for i, x in enumerate(part):
            for j, y in enumerate(part):
                square[i + j] = (square[i + j] + x * y) % 5

        if square != target:
            print(-1)
            return

        offset = low // 2
        root[offset:offset + len(part)] = part

    answers = []
    for sign in (1, -1):
        value = 0
        for i in range(size - 1, -1, -1):
            digit = sign * root[i] % 5
            if digit % 2 != parity[i]:
                digit += 5
            value = value * 10 + digit
        if value > 0:
            answers.append(value)

    print(min(answers) if answers else -1)


if __name__ == "__main__":
    main()