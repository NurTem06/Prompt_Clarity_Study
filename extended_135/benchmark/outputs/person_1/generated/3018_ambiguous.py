import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, target = data[0], data[1]
    dice = data[2:2 + k]
    total = sum(dice)

    if total == target:
        print(0)
        return

    reachable = [0] * (k + 1)
    reachable[0] = 1
    for i, value in enumerate(dice):
        for count in range(i + 1, 0, -1):
            reachable[count] |= reachable[count - 1] << value

    ways = [1]
    denominator = 1
    best_n = 0
    best_ways = 0
    best_denominator = 1
    offset = target - total

    for n in range(1, k + 1):
        next_ways = [0] * (6 * n + 1)
        for previous_sum, count in enumerate(ways):
            if count:
                for face in range(1, 7):
                    next_ways[previous_sum + face] += count
        ways = next_ways
        denominator *= 6

        maximum = 0
        possible_sums = reachable[n]
        while possible_sums:
            bit = possible_sums & -possible_sums
            old_sum = bit.bit_length() - 1
            needed = offset + old_sum
            if n <= needed <= 6 * n:
                maximum = max(maximum, ways[needed])
            possible_sums ^= bit

        if maximum * best_denominator > best_ways * denominator:
            best_n = n
            best_ways = maximum
            best_denominator = denominator

    print(best_n)


if __name__ == "__main__":
    main()