import sys

n, m = map(int, input().split())
Pocketmon_name = {}
Pocketmon_index = {}

for i in range(n):
    name = sys.stdin.readline().rstrip()
    Pocketmon_name[i] = name
    Pocketmon_index[name] = i

for i in range(m):
    answer = sys.stdin.readline().rstrip()
    if answer.isdigit():
        print(Pocketmon_name[int(answer) - 1])
    else:
        print(Pocketmon_index[answer] + 1)