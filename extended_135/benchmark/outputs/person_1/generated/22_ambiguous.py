import sys

s = sys.stdin.readline().strip()
mirror = {c: c for c in "AHIMOTUVWXYovwx"}
mirror.update({'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'})

print("TAK" if all(mirror.get(a) == b for a, b in zip(s, reversed(s))) else "NIE")
