A = []
row_size_A, col_size_A = map(int, input().split())
for _ in range(row_size_A):
    A.append(list(map(int, input().split())))
    
B = []
row_size_B, col_size_B = map(int, input().split())
for _ in range(row_size_B):
    B.append(list(map(int, input().split())))
    
result = [[0 for _ in range(col_size_B)] for _ in range(row_size_A)]
for i in range(row_size_A):
    for j in range(col_size_B):
        for k in range(col_size_A):
            result[i][j] += A[i][k] * B[k][j]

for i in result:
    print(*i)