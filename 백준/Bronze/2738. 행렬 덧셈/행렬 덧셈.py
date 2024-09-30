n, m = map(int, input().split())

A, B = [], []

for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

for _ in range(n):
    b = list(map(int, input().split()))
    B.append(b)
    
for i in range(n):
    for j in range(m):
        sum_col = A[i][j] + B[i][j]
        print(sum_col, end = " ")
    print()