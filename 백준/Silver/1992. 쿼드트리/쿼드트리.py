def sol(x, y, size):
    color = video[x][y] # 기준
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != video[i][j]:
                result.append('(')
                sol(x, y, size // 2)                            # 왼쪽 위
                sol(x, y + size // 2, size // 2)                # 오른쪽 위
                sol(x + size // 2, y, size // 2)                # 왼쪽 아래
                sol(x + size // 2, y + size // 2, size // 2)    # 오른쪽 아래
                result.append(')')
                return
    result.append(color)
                
size = int(input())
video = []
for _ in range(size):
    video.append(list(map(int, input().strip())))
    
result = []
sol(0, 0, size)
print(*result, sep = '')