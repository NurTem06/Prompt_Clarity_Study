import sys


def syllables(word):
    text = ''.join(c.lower() for c in word if c.isascii() and c.isalpha())
    units = []
    i = 0

    while i < len(text):
        c = text[i]
        if c == 'q' and i + 1 < len(text) and text[i + 1] == 'u':
            units.append(('q', False))
            i += 2
        else:
            vowel = c in 'aeiouy'
            if c == 'y' and i + 1 < len(text) and text[i + 1] in 'aeiou':
                vowel = False
            units.append((c, vowel))
            i += 1

    if units and units[-1][0] == 'e':
        keep = (
            len(units) >= 3
            and units[-2][0] == 'l'
            and not units[-3][1]
        )
        if not keep:
            units.pop()
    elif len(units) >= 2 and units[-2][0] == 'e' and units[-1][0] == 's':
        keep = len(units) >= 4 and not units[-3][1] and not units[-4][1]
        if not keep:
            units = units[:-2]

    count = 0
    previous_vowel = False
    for _, vowel in units:
        if vowel and not previous_vowel:
            count += 1
        previous_vowel = vowel

    return max(1, count)


def main():
    line = sys.stdin.readline().rstrip('\r\n')
    words = line.split(' ')
    total = 0
    cuts = []

    for i, word in enumerate(words):
        total += syllables(word)
        if total in (5, 12):
            cuts.append(i + 1)

    if total == 17 and len(cuts) == 2:
        a, b = cuts
        print(' '.join(words[:a]))
        print(' '.join(words[a:b]))
        print(' '.join(words[b:]))
    else:
        print(line)


if __name__ == '__main__':
    main()
