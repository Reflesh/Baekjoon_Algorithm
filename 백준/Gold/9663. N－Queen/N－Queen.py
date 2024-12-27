def check_attack(chess, row, col):
    for i in range(row):
        if chess[i] == col:
            return False
        if abs(chess[i] - col) == abs(i - row):
            return False
    
    return True

def sol(row):
    global cnt
    if row == N:
        cnt += 1
        return
    else:
        for col in range(N):
            chess[row] = col
            if check_attack(chess, row, col):
                sol(row + 1)

N = int(input())
chess = [0] * N
cnt = 0
sol(0)
print(cnt)