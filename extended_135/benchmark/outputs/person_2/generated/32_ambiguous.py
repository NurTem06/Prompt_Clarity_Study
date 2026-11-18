import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    position = 0
    valid = True

    for i in range(n):
        distance = int(data[1 + 2 * i])
        direction = data[2 + 2 * i]

        if direction == b"South":
            position += distance
        elif direction == b"North":
            position -= distance
        elif position == 0 or position == 20000:
            valid = False

        if position < 0 or position > 20000:
            valid = False

    print("YES" if valid and position == 0 else "NO")

if __name__ == "__main__":
    main()