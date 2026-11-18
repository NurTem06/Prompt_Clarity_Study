import sys

def main():
    n, m = map(int, sys.stdin.buffer.read().split())
    a, nr = divmod(n, 5)
    b, mr = divmod(m, 5)
    answer = 0
    for r in range(5):
        s = (-r) % 5
        count_n = a + (1 <= r <= nr)
        count_m = b + (1 <= s <= mr)
        answer += count_n * count_m
    print(answer)

if __name__ == "__main__":
    main()