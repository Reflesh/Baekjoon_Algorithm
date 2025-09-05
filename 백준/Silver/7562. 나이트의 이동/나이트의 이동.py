import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    chess[y][x] = 0
    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return chess[y][x]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and chess[ny][nx] == 0:
                chess[ny][nx] = chess[y][x] + 1
                queue.append((nx, ny))
        
                
case = int(input())
for _ in range(case):
    size = int(input())
    chess = [[0 for _ in range(size)] for _ in range(size)]
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(now_x, now_y))