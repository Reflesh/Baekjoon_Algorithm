import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def sol(x, y):
    if x == height-1 and y == width-1:
        return 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dir in range(4):
            new_x = dx[dir] + x
            new_y = dy[dir] + y
            if 0 <= new_x < height and 0<= new_y < width:
                if board[new_x][new_y] < board[x][y]:
                    dp[x][y] += sol(new_x, new_y)
    return dp[x][y]
                

height, width = map(int, input().split())
board = []
for i in range(height):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
dp = [[-1] * width for _ in range(height)]

print(sol(0, 0))