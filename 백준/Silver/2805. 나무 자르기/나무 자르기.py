import sys
input = sys.stdin.readline

Tree_num, need_length = map(int, input().split())
Tree = list(map(int, input().split()))

start, end = 1, max(Tree)
while start <= end:
    mid = (start + end) // 2
    get_Tree = 0
    for tr in Tree:
        if tr > mid: # 나무가 잘리는 경우
            get_Tree += tr - mid
    if get_Tree >= need_length: # 더 많은 나무를 가지게 되는 경우
        start = mid + 1
    else: # 목표치보다 더 작은 나무를 가지게 되는 경우
        end = mid - 1
        
print(end)