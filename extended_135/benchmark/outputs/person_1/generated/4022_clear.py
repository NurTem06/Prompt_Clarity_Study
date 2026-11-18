import sys


def main():
    read = sys.stdin.buffer.readline
    n = int(read())

    max_left = second_left = -1
    min_right = second_right = 10**18
    max_left_index = min_right_index = -1

    for i in range(n):
        left, right = map(int, read().split())

        if left > max_left:
            second_left = max_left
            max_left = left
            max_left_index = i
        elif left > second_left:
            second_left = left

        if right < min_right:
            second_right = min_right
            min_right = right
            min_right_index = i
        elif right < second_right:
            second_right = right

    if max_left_index == min_right_index:
        answer = second_right - second_left
    else:
        answer = max(min_right - second_left, second_right - max_left)

    print(max(0, answer))


if __name__ == "__main__":
    main()
