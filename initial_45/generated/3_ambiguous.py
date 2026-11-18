import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[0], data[1]

    intervals = []
    diff = [0] * (n + 2)
    for i in range(2, 2 + 2 * q, 2):
        l, r = data[i], data[i + 1]
        intervals.append((l, r))
        diff[l] += 1
        diff[r + 1] -= 1

    one = [0] * (n + 1)
    two = [0] * (n + 1)
    coverage = 0
    total = 0
    for x in range(1, n + 1):
        coverage += diff[x]
        total += coverage > 0
        one[x] = one[x - 1] + (coverage == 1)
        two[x] = two[x - 1] + (coverage == 2)

    painters = sorted(
        (one[r] - one[l - 1], l, r) for l, r in intervals
    )

    best_loss = total + 1
    for i in range(q - 1):
        unique_i, li, ri = painters[i]
        if 2 * unique_i >= best_loss:
            break

        for j in range(i + 1, q):
            unique_j, lj, rj = painters[j]
            loss = unique_i + unique_j
            if loss >= best_loss:
                break

            left = li if li > lj else lj
            right = ri if ri < rj else rj
            if left <= right:
                loss += two[right] - two[left - 1]

            if loss < best_loss:
                best_loss = loss
                if best_loss == 0:
                    print(total)
                    return

    print(total - best_loss)


if __name__ == "__main__":
    main()
