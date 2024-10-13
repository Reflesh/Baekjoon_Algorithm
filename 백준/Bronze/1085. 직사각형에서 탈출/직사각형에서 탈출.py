hansu_x, hansu_y, rec_x, rec_y = map(int, input().split())
print(min(hansu_x, hansu_y, rec_x - hansu_x, rec_y - hansu_y))