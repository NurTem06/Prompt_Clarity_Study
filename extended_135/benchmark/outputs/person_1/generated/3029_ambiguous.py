import sys
from array import array

MOD = 11092019
SHIFT = 24
MASK = (1 << SHIFT) - 1


def main():
    read = sys.stdin.buffer.readline
    line = read()
    if not line:
        return
    n = int(line)

    values = array('I', (int(read()) for _ in range(n)))
    maximum = max(values)

    ranks = array('I', [0]) * (maximum + 1)
    for x in values:
        ranks[x] = 1

    size = 0
    for x in range(maximum + 1):
        if ranks[x]:
            size += 1
            ranks[x] = size

    for i in range(n):
        values[i] = ranks[values[i]]
    del ranks

    parent = array('I', [0]) * n
    child = array('i', [-1]) * n
    sibling = array('i', [-1]) * n

    for i in range(1, n):
        p = int(read()) - 1
        parent[i] = p
        sibling[i] = child[p]
        child[p] = i

    bit = array('Q', [0]) * (size + 1)
    history = array('Q')
    changes = bytearray(n)

    answer_length = 0
    answer_count = 0
    v = 0

    while True:
        x = values[v]
        pos = x
        best_length = 0
        ways = 0

        while pos:
            entry = bit[pos]
            length = entry >> SHIFT
            if length > best_length:
                best_length = length
                ways = entry & MASK
            elif length == best_length:
                ways += entry & MASK
                if ways >= MOD:
                    ways -= MOD
            pos -= pos & -pos

        length = best_length + 1
        if best_length == 0:
            ways = 1

        if length > answer_length:
            answer_length = length
            answer_count = ways
        elif length == answer_length:
            answer_count += ways
            if answer_count >= MOD:
                answer_count -= MOD

        packed = (length << SHIFT) | ways
        pos = x
        changed = 0

        while pos <= size:
            old = bit[pos]
            old_length = old >> SHIFT
            if old_length > length:
                break

            history.append(old)
            changed += 1

            if old_length == length:
                count = (old & MASK) + ways
                if count >= MOD:
                    count -= MOD
                bit[pos] = (length << SHIFT) | count
            else:
                bit[pos] = packed

            pos += pos & -pos

        changes[v] = changed

        if child[v] != -1:
            v = child[v]
            continue

        while True:
            start = len(history) - changes[v]
            pos = values[v]
            for i in range(start, len(history)):
                bit[pos] = history[i]
                pos += pos & -pos
            del history[start:]

            nxt = sibling[v]
            if nxt != -1:
                v = nxt
                break

            if v == 0:
                sys.stdout.write(f"{answer_length} {answer_count}\n")
                return
            v = parent[v]


if __name__ == "__main__":
    main()
