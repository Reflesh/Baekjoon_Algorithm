n, m = map(int, input().split())
chess = []
result = []

for _ in range(n): # 2차원 배열로 변환
    row = list(input().strip())
    chess.append(row)

for i in range(n - 7):
    for j in range(m - 7):
        count_1 = 0
        count_2 = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:  # 짝수 칸
                    if chess[x][y] != 'B':
                        count_1 += 1
                    if chess[x][y] != 'W':
                        count_2 += 1
                else:  # 홀수 칸
                    if chess[x][y] != 'W':
                        count_1 += 1
                    if chess[x][y] != 'B':
                        count_2 += 1

        result.append(count_1)
        result.append(count_2)

print(min(result))