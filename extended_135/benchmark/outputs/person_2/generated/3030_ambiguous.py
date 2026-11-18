import sys
import random

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
base = n + 1

keys = [0] * (n + 1)
parents = [0] * (n + 1)
for i in range(1, n + 1):
    keys[i] = data[2 * i - 1] * base + i
    parents[i] = data[2 * i]
del data

left = [0] * (n + 1)
right = [0] * (n + 1)
priority = [0] + [random.getrandbits(64) + 1 for _ in range(n)]
roots = [0] * (n + 1)


def split(t, key):
    if not t:
        return 0, 0
    if keys[t] < key:
        a, b = split(right[t], key)
        right[t] = a
        return t, b
    a, b = split(left[t], key)
    left[t] = b
    return a, t


def unite(a, b):
    if not a:
        return b
    if not b:
        return a
    if priority[a] < priority[b]:
        a, b = b, a
    x, y = split(b, keys[a])
    left[a] = unite(left[a], x)
    right[a] = unite(right[a], y)
    return a


def insert_between(a, b, node):
    p = priority[node]
    if a and priority[a] > p and (not b or priority[a] > priority[b]):
        right[a] = insert_between(right[a], b, node)
        return a
    if b and priority[b] > p:
        left[b] = insert_between(a, left[b], node)
        return b
    left[node] = a
    right[node] = b
    return node


answer = n

for i in range(n, 0, -1):
    a, b = split(roots[i], keys[i])

    if b:
        answer -= 1
        if not left[b]:
            b = right[b]
        else:
            current = b
            while left[left[current]]:
                current = left[current]
            removed = left[current]
            left[current] = right[removed]

    root = insert_between(a, b, i)
    parent = parents[i]
    if parent:
        roots[parent] = unite(roots[parent], root)

print(answer)
