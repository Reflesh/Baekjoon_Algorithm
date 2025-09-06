import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for i in range(length):
        for j in range(width):
            if storage[i][j] == 1:
                queue.append([i, j])
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < width and storage[nx][ny] == 0:
                storage[nx][ny] = storage[x][y] + 1
                queue.append((nx, ny))
        
                
width, length = map(int, input().split())
storage = [list(map(int, input().split())) for _ in range(length)]

bfs()

day = 0
for i in range(length):
    for j in range(width):
        if storage[i][j] == 0: # 토마토를 다 익히지 못한 경우
            print(-1)
            exit()
    day = max(day, max(storage[i]))
    
print(day-1)