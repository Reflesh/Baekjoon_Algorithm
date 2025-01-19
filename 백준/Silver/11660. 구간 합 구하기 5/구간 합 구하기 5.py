import sys

size, cnt = map(int, input().split())
board = []

for _ in range(size):
    board.append(list(map(int, sys.stdin.readline().split())))
    
result = [[0] * (size + 1) for _ in range(size + 1)]
for i in range(size + 1): # 누적 합 저장
    for j in range(size + 1):
        result[i][j] = result[i][j-1] + result[i-1][j] - result[i-1][j-1] + board[i-1][j-1]
        
for i in range(cnt): # 구간 합 구하기
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = result[x2][y2] - result[x2][y1-1] - result[x1-1][y2] + result[x1-1][y1-1] # 겹치는 부분 더하기
    print(answer)