import sys

def main():
    x, hh, mm = map(int, sys.stdin.buffer.read().split())
    time = hh * 60 + mm
    presses = 0

    while True:
        h, m = divmod(time, 60)
        if '7' in f'{h:02d}{m:02d}':
            print(presses)
            return
        time = (time - x) % 1440
        presses += 1

if __name__ == "__main__":
    main()
