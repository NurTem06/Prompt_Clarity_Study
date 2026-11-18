import sys


def main():
    data = sys.stdin.buffer
    line = data.readline()
    if not line:
        return
    n = int(line)

    ids = {}
    parent = []
    inequalities = []

    def get_id(word):
        key = word[-3:]
        index = ids.get(key)
        if index is None:
            index = len(parent)
            ids[key] = index
            parent.append(-1)
        return index

    def find(x):
        root = x
        while parent[root] >= 0:
            root = parent[root]
        while x != root:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if parent[a] > parent[b]:
            a, b = b, a
        parent[a] += parent[b]
        parent[b] = a

    for _ in range(n):
        x, relation, y = data.readline().split()
        a = get_id(x)
        b = get_id(y)
        if relation == b'is':
            union(a, b)
        else:
            inequalities.append((a, b))

    for suffix, index in ids.items():
        if len(suffix) >= 2:
            short_id = ids.get(suffix[-1:])
            if short_id is not None:
                union(index, short_id)
        if len(suffix) == 3:
            short_id = ids.get(suffix[-2:])
            if short_id is not None:
                union(index, short_id)

    for a, b in inequalities:
        if find(a) == find(b):
            sys.stdout.write("wait what?\n")
            return

    sys.stdout.write("yes\n")


if __name__ == "__main__":
    main()
