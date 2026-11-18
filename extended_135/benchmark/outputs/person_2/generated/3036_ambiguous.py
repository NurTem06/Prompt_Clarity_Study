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
        ingredients = set()
        for _ in range(k):
            ingredient = next(it) - 1
            if brands[ingredient] > 1:
                ingredients.add(ingredient)
        dishes.append(ingredients)

    incompatible = [set() for _ in dishes]
    for _ in range(n):
        a, b = next(it) - 1, next(it) - 1
        incompatible[a].add(b)
        incompatible[b].add(a)

    limit = 10**18
    total = 0

    for starter in range(s):
        for main_dish in range(s, s + m):
            if main_dish in incompatible[starter]:
                continue
            first_two = dishes[starter] | dishes[main_dish]
            for dessert in range(s + m, s + m + d):
                if (dessert in incompatible[starter] or
                        dessert in incompatible[main_dish]):
                    continue

                ways = 1
                for ingredient in first_two | dishes[dessert]:
                    ways *= brands[ingredient]
                    if ways > limit - total:
                        print("too many")
                        return
                total += ways
                if total > limit:
                    print("too many")
                    return

    print(total)


if __name__ == "__main__":
    main()
