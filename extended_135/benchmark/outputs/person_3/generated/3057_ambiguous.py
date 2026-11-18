import sys


def main():
    read = sys.stdin.buffer.readline
    first = read()
    if not first:
        return

    n = int(first)
    ids = {}
    parent = []
    size = []
    inequalities = []

    def get_id(word):
        idx = ids.get(word)
        if idx is None:
            idx = len(parent)
            ids[word] = idx
            parent.append(idx)
            size.append(1)
        return idx

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    for _ in range(n):
        left, relation, right = read().split()
        a = get_id(left)
        b = get_id(right)
        if relation == b'is':
            union(a, b)
        else:
            inequalities.append((a, b))

    suffix_groups = {}
    for word, idx in ids.items():
        suffix = word[-3:]
        representative = suffix_groups.get(suffix)
        if representative is None:
            suffix_groups[suffix] = idx
        else:
            union(idx, representative)

    for suffix, representative in suffix_groups.items():
        short = ids.get(suffix[-1:])
        if short is not None:
            union(representative, short)

        if len(suffix) >= 2:
            short = ids.get(suffix[-2:])
            if short is not None:
                union(representative, short)

    for a, b in inequalities:
        if find(a) == find(b):
            sys.stdout.write("wait what?\n")
            return

    sys.stdout.write("yes\n")


if __name__ == "__main__":
    main()
