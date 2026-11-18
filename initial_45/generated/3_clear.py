import sys
from math import isqrt


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    count_diff = [0] * (n + 2)
    sum_diff = [0] * (n + 2)
    square_diff = [0] * (n + 2)

    pos = 2
    for painter in range(1, q + 1):
        left, right = data[pos], data[pos + 1]
        pos += 2
        end = right + 1
        square = painter * painter

        count_diff[left] += 1
        count_diff[end] -= 1
        sum_diff[left] += painter
        sum_diff[end] -= painter
        square_diff[left] += square
        square_diff[end] -= square

    unique = [0] * (q + 1)
    pair_loss = {}
    base = q + 1
    count = id_sum = square_sum = painted = 0

    for section in range(1, n + 1):
        count += count_diff[section]
        id_sum += sum_diff[section]
        square_sum += square_diff[section]

        if count:
            painted += 1
        if count == 1:
            unique[id_sum] += 1
        elif count == 2:
            difference = isqrt(2 * square_sum - id_sum * id_sum)
            first = (id_sum - difference) // 2
            second = (id_sum + difference) // 2
            key = first * base + second
            pair_loss[key] = pair_loss.get(key, 0) + 1

    ordered = sorted((unique[i], i) for i in range(1, q + 1))
    best_loss = painted

    for i in range(q - 1):
        first_loss, first = ordered[i]
        if first_loss + ordered[i + 1][0] >= best_loss:
            break

        for j in range(i + 1, q):
            second_loss, second = ordered[j]
            loss = first_loss + second_loss
            if loss >= best_loss:
                break

            if first < second:
                key = first * base + second
            else:
                key = second * base + first

            extra = pair_loss.get(key, 0)
            candidate = loss + extra
            if candidate < best_loss:
                best_loss = candidate
            if extra == 0:
                break

    print(painted - best_loss)


if __name__ == "__main__":
    main()
