import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        if campus[x][y] == 'P':
            cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return cnt

row, col = map(int, input().split())
campus = [list(input().strip()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

start_x = start_y = -1
for i in range(row):
    for j in range(col):
        if campus[i][j] == 'I':
            start_x, start_y = i, j

result = bfs(start_x, start_y)
if result == 0:
    print("TT")
else:
    print(result)