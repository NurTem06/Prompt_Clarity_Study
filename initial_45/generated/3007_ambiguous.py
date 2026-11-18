import sys


def main():
    d, b, f, t0, t1, t2 = map(int, sys.stdin.buffer.read().split())

    value = [1] * d
    for day in range(d - 4, -1, -1):
        value[day] = 3 * sum(value[day + 3::3])

    baseline = b // 100 + f * value[0]
    for phase, trees in enumerate((t0, t1, t2)):
        baseline += 3 * trees * sum(value[phase::3])

    initial = (
        b // 100
        | (min(t0, 5) << 4)
        | (min(t1, 5) << 7)
        | (min(t2, 5) << 10)
    )
    dp = {initial: 0}

    for day in range(d):
        ndp = {}
        multiplier = value[day]
        sale_cost = 1 - multiplier
        investment_gain = 5 * multiplier - 4
        extra = min(f, 20) if day == 0 else 0
        can_invest = day + 3 < d

        for state, score in dp.items():
            cash = state & 15
            ordinary = (state >> 4) & 7
            next_ordinary = (state >> 7) & 7
            later_ordinary = (state >> 10) & 7
            exotic = (state >> 13) & 1
            next_exotic = (state >> 14) & 1
            later_exotic = (state >> 15) & 1

            available = 3 * ordinary + extra
            grown = ordinary + available
            rotated = (
                (next_ordinary << 4)
                | (later_ordinary << 7)
                | (next_exotic << 13)
                | (later_exotic << 14)
                | (exotic << 15)
            )

            max_ordinary_sale = min(available, 15 - cash)
            for sold_ordinary in range(max_ordinary_sale + 1):
                new_ordinary = min(5, grown - sold_ordinary)
                base_state = rotated | (new_ordinary << 10)
                money = cash + sold_ordinary
                partial_score = score + sold_ordinary * sale_cost
                max_exotic_sale = min(3 * exotic, (15 - money) // 5)

                for sold_exotic in range(max_exotic_sale + 1):
                    balance = money + 5 * sold_exotic
                    current_score = partial_score + 5 * sold_exotic * sale_cost

                    key = base_state | balance
                    previous = ndp.get(key)
                    if previous is None or current_score > previous:
                        ndp[key] = current_score

                    if balance >= 4:
                        key = base_state | min(15, balance + 1)
                        candidate = current_score + 1
                        previous = ndp.get(key)
                        if previous is None or candidate > previous:
                            ndp[key] = candidate

                        if can_invest:
                            key = base_state | (1 << 15) | (balance - 4)
                            candidate = current_score + investment_gain
                            previous = ndp.get(key)
                            if previous is None or candidate > previous:
                                ndp[key] = candidate

        dp = ndp

    print((baseline + max(dp.values())) * 100 + b % 100)


if __name__ == "__main__":
    main()
