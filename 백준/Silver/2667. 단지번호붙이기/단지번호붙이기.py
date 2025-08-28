import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global count
    if x < 0 or x >= size or y < 0 or y >= size:
        return
    if Complex[x][y] == 1:
        count += 1
        Complex[x][y] = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            dfs(xx, yy)

Complex = []
size = int(input())
for _ in range(size):
    Complex.append(list(map(int, input().strip())))
    
result = []
count = 0
for i in range(size):
    for j in range(size):
        if Complex[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0
            
result.sort()
print(len(result))
for k in result:
    print(k)