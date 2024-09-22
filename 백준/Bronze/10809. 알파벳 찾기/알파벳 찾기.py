loc = [-1] * 26
ch = list(input())
for i, ch in enumerate(ch):
    ch_ = ord(ch) - 97
    if loc[ch_] == -1:
        loc[ch_] = i

print(*loc)