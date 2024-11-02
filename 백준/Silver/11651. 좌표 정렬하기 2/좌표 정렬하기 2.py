n = int(input())
loc_list = []

for i in range(n):
    x, y = map(int, input().split())
    loc_list.append((x, y))

loc_list.sort(key = lambda x: (x[1], x[0]))

for x, y in loc_list:
    print(x, y)