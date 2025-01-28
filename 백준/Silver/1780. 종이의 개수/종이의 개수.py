def sol(x, y, size):
    global minus, zero, one
    color = paper[x][y] # 기준
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 위의 형식으로 재귀함수 호출
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != paper[i][j]:
                sol(x, y, size // 3)                                  # 1
                sol(x, y + size // 3, size // 3)                      # 2
                sol(x, y + size * 2 // 3, size // 3)                  # 3
                sol(x + size // 3, y, size // 3)                      # 4
                sol(x + size // 3, y + size // 3, size // 3)          # 5
                sol(x + size // 3, y + size * 2 // 3, size // 3)      # 6
                sol(x + size * 2 // 3, y, size // 3)                  # 7
                sol(x + size * 2 // 3, y + size // 3, size // 3)      # 8
                sol(x + size * 2 // 3, y + size * 2 // 3, size // 3)  # 9
                return
    if color == -1:
        minus += 1
    elif color == 0:
        zero += 1
    elif color == 1:
        one += 1
        
                
size = int(input())
paper = []
for _ in range(size):
    paper.append(list(map(int, input().split())))
    
minus, zero, one = 0, 0, 0
sol(0, 0, size)
print(minus, zero, one, sep = "\n")