import sys
from math import gcd

def main():
    data = sys.stdin.buffer.read().split()
    g = 0
    for value in data[1:]:
        g = gcd(g, int(value))
        if g == 1:
            print(1)
            return

    answer = 1
    exponent = 0
    while g % 2 == 0:
        g //= 2
        exponent += 1
    answer *= exponent + 1

    divisor = 3
    while divisor * divisor <= g:
        if g % divisor == 0:
            exponent = 0
            while g % divisor == 0:
                g //= divisor
                exponent += 1
            answer *= exponent + 1
        divisor += 2

    if g > 1:
        answer *= 2

    print(answer)

if __name__ == "__main__":
    main()