import sys


def main():
    d, b, f, t0, t1, t2 = map(int, sys.stdin.buffer.read().split())
    cash, remainder = divmod(b, 100)
    trees = [t0, t1, t2]

    if d <= 3:
        for day in range(d):
            cash += 3 * trees[day]
            if day == 0:
                cash += f
            if cash >= 4:
                cash += 1
        print(cash * 100 + remainder)
        return

    initial_score = 0
    for i in range(3):
        if trees[i] > 4:
            initial_score += (trees[i] - 4) * 3 * (4 ** ((d - 1 - i) // 3))
            trees[i] = 4

    size = 13000
    bases = [0] * size
    transition_indices = [0] * size

    for key in range(size):
        state, c = divmod(key, 13)
        mask, normals = divmod(state, 125)
        n0 = normals % 5
        n1 = (normals // 5) % 5
        n2 = normals // 25
        bases[key] = 13 * (n1 + 5 * n2 + 125 * (mask >> 1))
        transition_indices[key] = (2 * n0 + (mask & 1)) * 13 + c

    def make_transitions(value, extra):
        result = [None] * 130
        for n in range(5):
            available_normal = 3 * n + extra
            for exotic_tree in range(2):
                available_exotic = 3 * exotic_tree
                for c in range(13):
                    best = {}
                    for sold_normal in range(min(12, available_normal) + 1):
                        total_normal_trees = n + available_normal - sold_normal
                        next_normal = min(4, total_normal_trees)
                        normal_surplus = total_normal_trees - next_normal

                        for sold_exotic in range(available_exotic + 1):
                            money = c + sold_normal + 5 * sold_exotic
                            total_exotic_trees = (
                                exotic_tree + available_exotic - sold_exotic
                            )

                            if money < 4:
                                next_exotic = min(1, total_exotic_trees)
                                surplus = normal_surplus + 5 * (
                                    total_exotic_trees - next_exotic
                                )
                                offset = (
                                    325 * next_normal + 6500 * next_exotic + money
                                )
                                reward = surplus * value
                                if reward > best.get(offset, -1):
                                    best[offset] = reward
                            else:
                                next_exotic = min(1, total_exotic_trees)
                                surplus = normal_surplus + 5 * (
                                    total_exotic_trees - next_exotic
                                )
                                new_cash = money + 1
                                overflow = max(0, new_cash - 12)
                                new_cash = min(12, new_cash)
                                offset = (
                                    325 * next_normal + 6500 * next_exotic + new_cash
                                )
                                reward = surplus * value + overflow
                                if reward > best.get(offset, -1):
                                    best[offset] = reward

                                planted_total = total_exotic_trees + 1
                                next_exotic = min(1, planted_total)
                                surplus = normal_surplus + 5 * (
                                    planted_total - next_exotic
                                )
                                new_cash = money - 4
                                overflow = max(0, new_cash - 12)
                                new_cash = min(12, new_cash)
                                offset = (
                                    325 * next_normal + 6500 * next_exotic + new_cash
                                )
                                reward = surplus * value + overflow
                                if reward > best.get(offset, -1):
                                    best[offset] = reward

                    index = (2 * n + exotic_tree) * 13 + c
                    result[index] = list(best.items())
        return result

    initial_key = 13 * (trees[0] + 5 * trees[1] + 25 * trees[2]) + cash
    dp = [-1] * size
    dp[initial_key] = initial_score
    active = [initial_key]
    cached_value = None
    cached_transitions = None

    for day in range(d - 3):
        value = 3 * (4 ** (((d - 1 - day) // 3) - 1))
        if day == 0 and f:
            transitions = make_transitions(value, f)
        else:
            if value != cached_value:
                cached_value = value
                cached_transitions = make_transitions(value, 0)
            transitions = cached_transitions

        next_dp = [-1] * size
        next_active = []
        for key in active:
            score = dp[key]
            base = bases[key]
            for offset, reward in transitions[transition_indices[key]]:
                target = base + offset
                candidate = score + reward
                previous = next_dp[target]
                if candidate > previous:
                    if previous == -1:
                        next_active.append(target)
                    next_dp[target] = candidate
        dp = next_dp
        active = next_active

    answer = 0
    for key in active:
        state, money = divmod(key, 13)
        mask, normals = divmod(state, 125)
        for _ in range(3):
            money += 3 * (normals % 5) + 15 * (mask & 1)
            if money >= 4:
                money += 1
            normals //= 5
            mask >>= 1
        total = dp[key] + money
        if total > answer:
            answer = total

    print(answer * 100 + remainder)


if __name__ == "__main__":
    main()