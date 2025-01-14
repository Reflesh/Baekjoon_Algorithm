num, weight = map(int, input().split())
result = [[0] * (weight + 1) for _ in range(num + 1)]
bag = []

for _ in range(num):
    bag.append(list(map(int, input().split())))
    
for i in range(1, num + 1):
    for j in range(1, weight + 1):
        if j >= bag[i-1][0]:
            result[i][j] = max(result[i-1][j], result[i][j-1], result[i-1][j-bag[i-1][0]] + bag[i-1][1])
        else:
            result[i][j] = result[i-1][j]
            
print(result[num][weight])