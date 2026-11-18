import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    total_gold = s.count(b'G')

    left = 0
    silvers = 0
    best = 0

    for right in range(n):
        if s[right] == 83:
            silvers += 1

        while silvers > 1:
            if s[left] == 83:
                silvers -= 1
            left += 1

        best = max(best, right - left + 1)

    print(min(best, total_gold))

if __name__ == "__main__":
    main()