table = []

for _ in range(5):
    row = list(input())
    table.append(row)
    max_row = max(len(row) for row in table)
    
for i in range(max_row):
    for j in range(5):
        try:
            print(table[j][i], end="")
        except IndexError:
            pass