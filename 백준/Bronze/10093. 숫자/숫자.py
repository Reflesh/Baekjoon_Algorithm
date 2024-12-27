start, end = map(int, input().split())
min_ls = min(start, end)
max_ls = max(start, end)
cnt = max_ls - min_ls - 1

if cnt + 1 <= 1:
    cnt = 0
print(cnt)
result = [i for i in range(min_ls + 1, max_ls)]
print(*result, end=' ')