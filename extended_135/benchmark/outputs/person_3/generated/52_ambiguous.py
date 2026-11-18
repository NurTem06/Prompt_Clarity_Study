import sys
from math import isqrt

def main():
    n = int(sys.stdin.buffer.readline())
    answers = set()
    power = 1

    while power <= n + 1:
        b = 2 * power - 3
        discriminant = b * b + 8 * n
        root = isqrt(discriminant)

        if root * root == discriminant:
            numerator = root - b
            if numerator > 0 and numerator % 2 == 0:
                odd_teams = numerator // 2
                if odd_teams % 2 == 1:
                    answers.add(odd_teams * power)

        power *= 2

    if answers:
        sys.stdout.write("\n".join(map(str, sorted(answers))))
    else:
        sys.stdout.write("-1")

if __name__ == "__main__":
    main()