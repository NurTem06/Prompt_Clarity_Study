import sys
from math import gcd

n, a, b, p, q = map(int, sys.stdin.buffer.read().split())
common = n // (a // gcd(a, b) * b)
print((n // a) * p + (n // b) * q - common * min(p, q))