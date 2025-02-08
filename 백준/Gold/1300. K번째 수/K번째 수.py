import sys
input = sys.stdin.readline

size = int(input()) 
find_num = int(input())

start = 1
end = find_num
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, size + 1):
        cnt += min(size, mid // i)
    if cnt < find_num:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)