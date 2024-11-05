n = int(input())
coordinate = list(map(int, input().split()))
sort_coord = sorted(list(set(coordinate)))
dic_coord = {}

for i in range(len(sort_coord)):
    dic_coord[sort_coord[i]] = i
    
for i in coordinate:
    print(dic_coord[i], end = ' ')