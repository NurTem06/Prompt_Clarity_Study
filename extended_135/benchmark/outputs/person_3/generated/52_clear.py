import sys
from math import isqrt

def main():
    n = int(sys.stdin.buffer.readline())
    answers = []
    power = 1

    while power <= n + 1:
        coefficient = 2 * power - 3
        discriminant = coefficient * coefficient + 8 * n
        root = isqrt(discriminant)

        if root * root == discriminant:
            difference = root - coefficient
            if difference > 0 and difference % 2 == 0:
                odd_teams = difference // 2
                if odd_teams & 1:
                    answers.append(power * odd_teams)

        power <<= 1

    answers.sort()
    sys.stdout.write("\n".join(map(str, answers)) if answers else "-1")

if __name__ == "__main__":
    main()