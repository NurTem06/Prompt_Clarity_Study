import sys
import random

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
base = n + 1

keys = [0] * base
parents = [0] * base
for i in range(1, base):
    keys[i] = data[2 * i - 1] * base + i
    parents[i] = data[2 * i]
del data

left = [0] * base
right = [0] * base
roots = [0] * base
rng = random.Random(712367821)
priority = [rng.getrandbits(64) for _ in range(base)]


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


def join(a, b):
    if not a:
        return b
    if not b:
        return a
    if priority[a] > priority[b]:
        right[a] = join(right[a], b)
        return a
    left[b] = join(a, left[b])
    return b


removed = False


def remove_ge(t, threshold):
    global removed
    if not t:
        return 0
    if keys[t] < threshold:
        right[t] = remove_ge(right[t], threshold)
    else:
        left[t] = remove_ge(left[t], threshold)
        if not removed:
            removed = True
            return join(left[t], right[t])
    return t


answer = n
for i in range(n, 0, -1):
    removed = False
    t = remove_ge(roots[i], keys[i] - i)
    if removed:
        answer -= 1
    t = unite(t, i)
    p = parents[i]
    if p:
        roots[p] = unite(roots[p], t)

print(answer)