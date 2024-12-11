import sys

N, M = map(int, input().split())
note = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word not in note:
            note[word] = 1
        else:
            note[word] += 1

result = sorted(note.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for wd, val in result:
    print(wd)