import sys
from array import array


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    labels = array('I', (int(read()) for _ in range(n)))

    parent = array('i', [-1]) * n
    child = array('i', [-1]) * n
    sibling = array('i', [-1]) * n

    for v in range(1, n):
        p = int(read()) - 1
        parent[v] = p
        sibling[v] = child[p]
        child[p] = v

    size = 1 << max(labels).bit_length()
    tree = [0] * (size << 1)
    previous = array('Q', [0]) * n

    MOD = 11092019
    BASE = 1 << 25
    MASK = BASE - 1

    answer = 0
    v = 0

    while True:
        pos = size + labels[v]
        previous[v] = tree[pos]

        result = tree[pos]
        q = pos
        while q > 1:
            if q & 1:
                other = tree[q - 1]
                if other:
                    if (other ^ result) < BASE:
                        result += other & MASK
                        if (result & MASK) >= MOD:
                            result -= MOD
                    elif other > result:
                        result = other
            q >>= 1

        value = result + BASE if result else BASE + 1

        if (answer ^ value) < BASE:
            answer += value & MASK
            if (answer & MASK) >= MOD:
                answer -= MOD
        elif value > answer:
            answer = value

        tree[pos] = value
        while pos > 1:
            other = tree[pos ^ 1]
            if other:
                if (other ^ value) < BASE:
                    value += other & MASK
                    if (value & MASK) >= MOD:
                        value -= MOD
                elif other > value:
                    value = other
            pos >>= 1
            if tree[pos] == value:
                break
            tree[pos] = value

        if child[v] != -1:
            v = child[v]
            continue

        while True:
            pos = size + labels[v]
            value = previous[v]
            tree[pos] = value

            while pos > 1:
                other = tree[pos ^ 1]
                if other:
                    if (other ^ value) < BASE:
                        value += other & MASK
                        if (value & MASK) >= MOD:
                            value -= MOD
                    elif other > value:
                        value = other
                pos >>= 1
                if tree[pos] == value:
                    break
                tree[pos] = value

            nxt = sibling[v]
            if nxt != -1:
                v = nxt
                break

            v = parent[v]
            if v == -1:
                print(answer >> 25, answer & MASK)
                return


if __name__ == "__main__":
    main()
