import sys

row, col, size = map(int, input().split())
chess = []

for _ in range(row): # 현재 보드판 저장
    chess.append(list(sys.stdin.readline().strip()))
    
prefix_sum = [[0] * (col + 1) for _ in range(row + 1)]

for x in range(1, row + 1):
    for y in range(1, col + 1):
        if (x + y) % 2 == 0:
            if chess[x-1][y-1] == 'B': # 변경할 필요가 없음
                prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1]
            else: # 변경이 필요하므로 +1 연산 추가
                prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1] + 1
        else:
            if chess[x-1][y-1] == 'W': # 변경할 필요가 없음
                prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1]
            else: # 변경이 필요하므로 +1 연산 추가
                prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1] + 1
                
result = size * size
for i in range(size, row + 1):
    for j in range(size, col + 1):
        # 현재 영역의 색상 변경 횟수를 계산
        tmp = prefix_sum[i][j] - prefix_sum[i-size][j] - prefix_sum[i][j-size] + prefix_sum[i-size][j-size]
        result = min(result, tmp, size*size-tmp) # 최솟값 갱신
        
print(result)