import sys
input = sys.stdin.readline

case_num = int(input())
matrix = []
for _ in range(case_num):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
    
#print(matrix)
sol = [[0] * case_num for _ in range(case_num)]
for len in range(1, case_num): # 구간의 범위 
    for i in range(case_num-len): # 시작 지점
        j = i + len
        sol[i][j] = 2**31
        for k in range(i, j): # k를 기준으로 최솟값 갱신
            sol[i][j] = min(sol[i][j], sol[i][k] + sol[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
            
print(sol[0][-1])