import sys
input = sys.stdin.readline

house_num, router = map(int, input().split())
house = []
for _ in range(house_num):
    house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prev_house = house[0]
    for i in range(1, house_num):
        if house[i] - prev_house >= mid: 
            cnt += 1 
            prev_house = house[i]
    if cnt >= router:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)