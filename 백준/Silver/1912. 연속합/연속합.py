n = int(input())
n_ls = list(map(int, input().split()))

for i in range(1, n):
    n_ls[i] = max(n_ls[i], n_ls[i] + n_ls[i-1])
print(max(n_ls))