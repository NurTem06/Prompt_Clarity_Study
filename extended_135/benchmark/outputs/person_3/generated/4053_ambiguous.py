import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pieces = data[1:]
    groups = [[] for _ in range(n)]

    for i, piece in enumerate(pieces):
        groups[len(piece)].append(i)

    a, b = (pieces[i] for i in groups[n - 1])

    for candidate in (a + b[-1:], b + a[-1:]):
        answer = [''] * (2 * n - 2)

        for length in range(1, n):
            i, j = groups[length]
            prefix = candidate[:length]
            suffix = candidate[-length:]

            if pieces[i] == prefix and pieces[j] == suffix:
                answer[i], answer[j] = 'P', 'S'
            elif pieces[j] == prefix and pieces[i] == suffix:
                answer[j], answer[i] = 'P', 'S'
            else:
                break
        else:
            sys.stdout.write(''.join(answer) + '\n')
            return


if __name__ == "__main__":
    main()