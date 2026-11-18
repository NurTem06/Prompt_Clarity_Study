import sys

a, b = map(int, sys.stdin.buffer.read().split())
price = max((100 * a + 7) // 8, 10 * b)

if price * 8 // 100 == a and price // 10 == b:
    print(price)
else:
    print(-1)