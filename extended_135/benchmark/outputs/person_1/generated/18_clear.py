import sys

s = sys.stdin.buffer.readline().strip()
n = len(s)

suffix_min = bytearray(n + 1)
suffix_min[n] = 123
for i in range(n - 1, -1, -1):
    suffix_min[i] = min(s[i], suffix_min[i + 1])

stack = []
result = bytearray()

for i, c in enumerate(s):
    stack.append(c)
    limit = suffix_min[i + 1]
    while stack and stack[-1] <= limit:
        result.append(stack.pop())

sys.stdout.buffer.write(result + b"\n")