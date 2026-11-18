import sys

def main():
    n = int(sys.stdin.buffer.read()) - 1
    answer = 0
    i = 1
    while i <= n:
        quotient = n // i
        last = n // quotient
        answer += quotient * (last - i + 1)
        i = last + 1
    print(answer)

if __name__ == "__main__":
    main()