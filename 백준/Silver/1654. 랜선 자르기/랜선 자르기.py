LAN, num = map(int, input().split())
LAN_length = []
for _ in range(LAN):
    LAN_length.append(int(input()))

start, end = 1, max(LAN_length)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for ln in LAN_length:
        cnt += ln // mid
    if cnt >= num: # 목표치보다 더 많은 랜선이 만들어지는 경우
        start = mid + 1
    else: # 목표치보다 더 작은 랜선이 만들어지는 경우
        end = mid - 1
        
print(end)