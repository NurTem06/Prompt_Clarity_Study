import sys

k = int(sys.stdin.buffer.read())
digits = 1
start = 1
count = 9

while k > digits * count:
    k -= digits * count
    digits += 1
    start *= 10
    count *= 10

number = start + (k - 1) // digits
index = (k - 1) % digits
print(str(number)[index])