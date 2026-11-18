import sys

def main():
    s = sys.stdin.buffer.readline().strip()
    left = s.find(b'[')
    right = s.rfind(b']')

    if left == -1 or right == -1 or left >= right:
        print(-1)
        return

    first_colon = s.find(b':', left + 1, right)
    last_colon = s.rfind(b':', left + 1, right)

    if first_colon == -1 or first_colon >= last_colon:
        print(-1)
    else:
        print(4 + s.count(b'|', first_colon + 1, last_colon))

if __name__ == "__main__":
    main()
