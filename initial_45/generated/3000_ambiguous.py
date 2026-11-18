import sys

MOD = 1_000_000_007


def main():
    tokens = sys.stdin.buffer.read().split()
    stack = []
    depth = 0
    value = 0

    for token in tokens[1:]:
        if token == b'(':
            stack.append(value)
            depth += 1
            value = 1 if depth & 1 else 0
        elif token == b')':
            inner = value
            value = stack.pop()
            depth -= 1
            if depth & 1:
                value = value * inner % MOD
            else:
                value += inner
                if value >= MOD:
                    value -= MOD
        else:
            number = int(token)
            if depth & 1:
                value = value * number % MOD
            else:
                value += number
                if value >= MOD:
                    value -= MOD

    print(value)


if __name__ == "__main__":
    main()
