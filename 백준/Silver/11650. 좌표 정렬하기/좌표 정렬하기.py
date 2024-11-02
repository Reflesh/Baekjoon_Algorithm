n = int(input())
loc_list = []

for i in range(n):
    x, y = map(int, input().split())
    loc_list.append((x, y))
    
loc_list_sorted = sorted(loc_list)

for x, y in loc_list_sorted:
    print(x, y)