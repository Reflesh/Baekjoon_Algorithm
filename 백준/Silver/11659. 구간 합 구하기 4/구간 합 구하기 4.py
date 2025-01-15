import sys

list_num, sum_num = map(int, input().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
sum_ls = [0] * (list_num + 1)

for i in range(list_num):
    sum_ls[i + 1] = sum_ls[i] + ls[i]

# print(sum_ls)
for _ in range(sum_num):
    start_index, end_index = map(int, sys.stdin.readline().rstrip().split())
    print(sum_ls[end_index] - sum_ls[start_index-1])