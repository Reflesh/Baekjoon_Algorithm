import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
                
    return maze[row-1][col-1]

row, col = map(int, input().split())
maze = []
for _ in range(row):
    maze.append(list(map(int, input().strip())))
print(bfs(0, 0))