import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    values = sorted(set(data[1:1 + data[0]]))
    count = len(values)

    if count == 1:
        answer = 0
    elif count == 2:
        gap = values[1] - values[0]
        answer = gap // 2 if gap % 2 == 0 else gap
    elif count == 3 and values[1] - values[0] == values[2] - values[1]:
        answer = values[1] - values[0]
    else:
        answer = -1

    print(answer)

if __name__ == "__main__":
    main()