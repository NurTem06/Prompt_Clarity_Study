import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

pattern = sys.stdin.buffer.read().strip()
total = 1
count = 1

for move in pattern:
    if move == 76:      # L
        total *= 2
    elif move == 82:    # R
        total = total * 2 + count
    elif move == 42:    # *
        total = total * 5 + count
        count *= 3

sys.stdout.write(str(total) + "\n")