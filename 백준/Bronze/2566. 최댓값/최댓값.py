table = []

for _ in range(9):
    row = list(map(int, input().split()))
    table.append(row)
    
max_num, max_row, max_col = -1, 0, 0
# max_num이 0일 경우 모든 행렬이 0일때 오류 발생

for r in range(9):
    for c in range(9):
        if max_num < table[r][c]:
            max_num = table[r][c]
            max_row = r + 1
            max_col = c + 1
            
print(max_num)
print(max_row, max_col)