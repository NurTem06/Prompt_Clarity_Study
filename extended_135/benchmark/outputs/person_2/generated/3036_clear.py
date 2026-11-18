import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    r, s, m, d, n = (next(it) for _ in range(5))
    brands = [next(it) for _ in range(r)]

    dishes = []
    for _ in range(s + m + d):
        k = next(it)
        dishes.append({next(it) - 1 for _ in range(k)})

    count = s + m + d
    incompatible = [[False] * count for _ in range(count)]
    for _ in range(n):
        a, b = next(it) - 1, next(it) - 1
        incompatible[a][b] = True
        incompatible[b][a] = True

    limit = 10**18
    total = 0

    for starter in range(s):
        for main_dish in range(s, s + m):
            if incompatible[starter][main_dish]:
                continue
            ingredients = dishes[starter] | dishes[main_dish]

            for dessert in range(s + m, count):
                if incompatible[starter][dessert] or incompatible[main_dish][dessert]:
                    continue

                ways = 1
                for ingredient in ingredients | dishes[dessert]:
                    ways *= brands[ingredient]
                    if ways > limit - total:
                        print("too many")
                        return
                total += ways

    print(total)


if __name__ == "__main__":
    main()
