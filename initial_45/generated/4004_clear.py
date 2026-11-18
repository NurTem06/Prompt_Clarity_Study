import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    values = sorted(set(data[1:1 + data[0]]))
    count = len(values)

    if count == 1:
        print(0)
    elif count == 2:
        difference = values[1] - values[0]
        print(difference // 2 if difference % 2 == 0 else difference)
    elif count == 3 and values[1] - values[0] == values[2] - values[1]:
        print(values[1] - values[0])
    else:
        print(-1)

if __name__ == "__main__":
    main()