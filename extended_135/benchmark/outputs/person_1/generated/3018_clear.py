import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, target = data[:2]
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

    powers = [1] * (k + 1)
    for i in range(1, k + 1):
        powers[i] = powers[i - 1] * 6

    distribution = [1]
    difference = target - total
    best_score = -1
    answer = 0

    for count in range(1, k + 1):
        next_distribution = [0] * (6 * count + 1)
        for previous_sum, ways in enumerate(distribution):
            if ways:
                for face in range(1, 7):
                    next_distribution[previous_sum + face] += ways
        distribution = next_distribution

        best_ways = 0
        sums = reachable[count]
        while sums:
            bit = sums & -sums
            removed_sum = bit.bit_length() - 1
            needed = difference + removed_sum
            if count <= needed <= 6 * count:
                best_ways = max(best_ways, distribution[needed])
            sums ^= bit

        score = best_ways * powers[k - count]
        if score > best_score:
            best_score = score
            answer = count

    print(answer)


if __name__ == "__main__":
    main()
