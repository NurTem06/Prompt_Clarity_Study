import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]
    left, right = 0, n - 1
    last = 0
    moves = []

    while left <= right:
        lv, rv = a[left], a[right]

        if lv <= last and rv <= last:
            break

        if lv > last and rv > last and lv == rv:
            i = left
            prev = last
            while i <= right and a[i] > prev:
                prev = a[i]
                i += 1
            left_count = i - left

            i = right
            prev = last
            while i >= left and a[i] > prev:
                prev = a[i]
                i -= 1
            right_count = right - i

            if left_count >= right_count:
                moves.extend("L" * left_count)
            else:
                moves.extend("R" * right_count)
            break

        if lv > last and (rv <= last or lv < rv):
            moves.append("L")
            last = lv
            left += 1
        else:
            moves.append("R")
            last = rv
            right -= 1

    sys.stdout.write(str(len(moves)) + "\n" + "".join(moves) + "\n")


if __name__ == "__main__":
    main()