import sys
from math import gcd

n, a, b, p, q = map(int, sys.stdin.buffer.read().split())
lcm = a // gcd(a, b) * b
print((n // a) * p + (n // b) * q - (n // lcm) * min(p, q))
