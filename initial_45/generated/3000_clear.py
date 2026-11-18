import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    mod = 1_000_000_007
    stack = []
    value = 0
    multiply = False

    for token in tokens[1:]:
        if token == b'(':
            stack.append(value)
            multiply = not multiply
            value = 1 if multiply else 0
        elif token == b')':
            parent = stack.pop()
            multiply = not multiply
            if multiply:
                value = parent * value % mod
            else:
                value = (parent + value) % mod
        else:
            number = int(token)
            if multiply:
                value = value * number % mod
            else:
                value = (value + number) % mod

    print(value)

if __name__ == "__main__":
    main()
