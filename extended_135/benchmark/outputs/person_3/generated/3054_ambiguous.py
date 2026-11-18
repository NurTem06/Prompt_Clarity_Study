import sys


def syllables(token):
    word = ''.join(c.lower() for c in token if c.isalpha())
    n = len(word)
    if not n:
        return 1

    vowels = [False] * n
    for i, c in enumerate(word):
        if c in 'aeiou':
            vowels[i] = not (c == 'u' and i > 0 and word[i - 1] == 'q')
        elif c == 'y':
            vowels[i] = i + 1 == n or word[i + 1] not in 'aeiou'

    def syllabic_le(e):
        return (
            e >= 2
            and word[e - 1] == 'l'
            and not vowels[e - 2]
        )

    if word.endswith('e'):
        e = n - 1
        if not syllabic_le(e):
            vowels[e] = False
    elif word.endswith('es'):
        e = n - 2
        prefix = word[:e]
        pronounced = (
            prefix.endswith(('s', 'x', 'z', 'c', 'g', 'ch', 'sh'))
            or syllabic_le(e)
        )
        if not pronounced:
            vowels[e] = False

    count = sum(
        vowel and (i == 0 or not vowels[i - 1])
        for i, vowel in enumerate(vowels)
    )
    return max(1, count)


def main():
    text = sys.stdin.readline().rstrip('\r\n')
    words = text.split(' ')
    counts = [syllables(word) for word in words]

    boundaries = []
    total = 0
    for i, count in enumerate(counts):
        total += count
        if total in (5, 12):
            boundaries.append(i + 1)

    if total == 17 and len(boundaries) == 2:
        first, second = boundaries
        print(' '.join(words[:first]))
        print(' '.join(words[first:second]))
        print(' '.join(words[second:]))
    else:
        print(text)


if __name__ == '__main__':
    main()
