import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    if x < 0 or x >= width or y < 0 or y >= length:
        return
    if field[y][x] == 1:
        field[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

num = int(input())
while num:
    width, length, cab_num = map(int, input().split())
    field = [[0 for _ in range(width)] for _ in range(length)]
    for _ in range(cab_num):
        index_x, index_y = map(int, input().split())
        field[index_y][index_x] = 1
    count = 0
    for i in range(length):
        for j in range(width):
            if field[i][j] == 1:
                dfs(j, i)
                count += 1
    print(count)
    num -= 1