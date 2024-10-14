rec_x, rec_y = [], []

for _ in range(3):
    x, y = map(int, input().split())
    rec_x.append(x)
    rec_y.append(y)

for i in range(3):
    if rec_x.count(rec_x[i]) == 1:
        result_x = rec_x[i]
    if rec_y.count(rec_y[i]) == 1:
        result_y = rec_y[i]

print(result_x, result_y)