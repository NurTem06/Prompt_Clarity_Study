import sys
from array import array


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + 2 * n]
    del data

    total = 3 * n
    edge1 = array('i', [-1]) * total
    edge2 = array('i', [-1]) * total

    for values, base, original_edges in (
        (a, n, edge1),
        (b, 2 * n, edge2),
    ):
        order = sorted(range(n), key=values.__getitem__)
        j = 0
        for pos, vertex in enumerate(order):
            limit = values[vertex] + k
            while j < n and values[order[j]] <= limit:
                j += 1
            if j < n:
                original_edges[vertex] = base + j

            chain_vertex = base + pos
            edge1[chain_vertex] = vertex
            if pos + 1 < n:
                edge2[chain_vertex] = chain_vertex + 1

    del a, b, values, order, original_edges

    discovery = array('i', [-1]) * total
    low = array('i', [0]) * total
    active = bytearray(total)
    progress = bytearray(total)
    component_stack = []
    dfs = []
    timer = 0
    answer = 0

    for start in range(total):
        if discovery[start] != -1:
            continue

        discovery[start] = low[start] = timer
        timer += 1
        active[start] = 1
        component_stack.append(start)
        dfs.append(start)

        while dfs:
            vertex = dfs[-1]
            state = progress[vertex]

            if state < 2:
                progress[vertex] = state + 1
                target = edge1[vertex] if state == 0 else edge2[vertex]
                if target == -1:
                    continue

                if discovery[target] == -1:
                    discovery[target] = low[target] = timer
                    timer += 1
                    active[target] = 1
                    component_stack.append(target)
                    dfs.append(target)
                elif active[target] and discovery[target] < low[vertex]:
                    low[vertex] = discovery[target]
            else:
                dfs.pop()

                if low[vertex] == discovery[vertex]:
                    contains_original = False
                    while True:
                        member = component_stack.pop()
                        active[member] = 0
                        if member < n:
                            contains_original = True
                        if member == vertex:
                            break
                    if contains_original:
                        answer += 1

                if dfs:
                    parent = dfs[-1]
                    if low[vertex] < low[parent]:
                        low[parent] = low[vertex]

    print(answer)


if __name__ == "__main__":
    main()
