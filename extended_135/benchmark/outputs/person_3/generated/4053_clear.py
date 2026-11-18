import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    strings = data[1:]
    groups = [[] for _ in range(n)]
    for i, value in enumerate(strings):
        groups[len(value)].append(i)

    a, b = (strings[i] for i in groups[n - 1])

    for candidate in (a + b[-1:], b + a[-1:]):
        answer = [''] * (2 * n - 2)
        valid = True

        for length in range(1, n):
            i, j = groups[length]
            prefix = candidate[:length]
            suffix = candidate[-length:]

            if strings[i] == prefix and strings[j] == suffix:
                answer[i], answer[j] = 'P', 'S'
            elif strings[j] == prefix and strings[i] == suffix:
                answer[j], answer[i] = 'P', 'S'
            else:
                valid = False
                break

        if valid:
            print(''.join(answer))
            return


if __name__ == "__main__":
    main()