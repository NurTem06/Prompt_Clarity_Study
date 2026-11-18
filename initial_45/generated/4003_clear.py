import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:n + 1]
    left, right = 0, n - 1
    last = 0
    moves = []

    while left <= right:
        lv, rv = a[left], a[right]

        if lv <= last and rv <= last:
            break

        if lv == rv:
            if lv <= last:
                break

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
                moves.append('L' * left_count)
            else:
                moves.append('R' * right_count)
            break

        if lv > last and (rv <= last or lv < rv):
            moves.append('L')
            last = lv
            left += 1
        else:
            moves.append('R')
            last = rv
            right -= 1

    answer = ''.join(moves)
    sys.stdout.write(str(len(answer)) + '\n' + answer + '\n')


if __name__ == '__main__':
    main()
