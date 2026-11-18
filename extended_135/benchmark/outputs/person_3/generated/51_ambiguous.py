import sys

t = sys.stdin.readline().strip()
n = len(t)

for length in range(n // 2 + 1, n):
    if t[:length] == t[n - length:]:
        print("YES")
        print(t[:length])
        break
else:
    print("NO")