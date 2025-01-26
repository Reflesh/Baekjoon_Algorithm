def sol(x, y, size):
    global white, blue
    color = square[x][y] # 기준
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != square[i][j]: # 색이 다른 경우
                sol(x, y, size // 2)                            # 1사분면
                sol(x, y + size // 2, size // 2)                # 2사분면
                sol(x + size // 2, y, size // 2)                # 3사분면
                sol(x + size // 2, y + size // 2, size // 2)    # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1
                
size = int(input())
square = []
white, blue = 0, 0
for _ in range(size):
    square.append(list(map(int, input().split())))
    
sol(0, 0, size)
print(white)
print(blue)