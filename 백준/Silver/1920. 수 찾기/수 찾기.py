def binary_sort(N):
    left_idx = 0
    right_idx = num - 1
    while left_idx <= right_idx:
        mid = (left_idx + right_idx) // 2
        if N > res[mid]:
            left_idx = mid + 1
        elif N < res[mid]:
            right_idx = mid - 1
        else: # 값을 찾은 경우
            return 1
    return 0 # 값을 찾지 못한 경우
        

num = int(input())
res = list(map(int, input().split()))
res.sort()

M = int(input())
cmp = list(map(int, input().split()))

for i in cmp:
    print(binary_sort(i))