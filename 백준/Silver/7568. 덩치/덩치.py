import sys
input = sys.stdin.readline

num = int(input())
people_info = []
for _ in range(num):
    height, weight = map(int, input().split())
    people_info.append([height, weight])
    
#print(people_info)
rank_info = []
for info in people_info:
    rank = 1
    for size in people_info:
        if info[0] < size[0] and info[1] < size[1]:
            rank += 1
    rank_info.append(rank)

print(*rank_info)