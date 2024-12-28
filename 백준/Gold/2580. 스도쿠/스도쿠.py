def check_square(x, y, t):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if t == sudoku[i][j]:
                return False
    return True

def check_row(x, t):
    for i in range(9):
        if t == sudoku[x][i]:
            return False
    return True

def checK_col(y, t):
    for i in range(9):
        if t == sudoku[i][y]:
            return False
    return True

def sol(idx):
    if idx == len(zero_idx):
        for i in sudoku:
            print(*i)
        exit()
    x, y = zero_idx[idx]
    for t in range(1, 10):
        if check_square(x - x % 3, y - y % 3, t) and check_row(x, t) and checK_col(y, t):
            sudoku[x][y] = t 
            sol(idx + 1)
            sudoku[x][y] = 0
    

sudoku = []
for _ in range(9):
    ls = list(map(int, input().split()))
    sudoku.append(ls)

zero_idx = []
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            zero_idx.append((x, y))
sol(0)