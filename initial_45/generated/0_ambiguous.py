import sys

s = sys.stdin.buffer.readline().strip()

left_bracket = s.find(b'[')
right_bracket = s.rfind(b']')

if left_bracket == -1 or right_bracket == -1:
    print(-1)
else:
    left_colon = s.find(b':', left_bracket + 1)
    right_colon = s.rfind(b':', 0, right_bracket)
    if left_colon == -1 or right_colon <= left_colon:
        print(-1)
    else:
        print(4 + s.count(b'|', left_colon + 1, right_colon))