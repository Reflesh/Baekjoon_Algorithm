num = int(input())
point = []

for _ in range(num):
    point.append(list(map(int, input().split())))
    
point = sorted(point, key = lambda x : x[0])
result = [1] * num

for i in range(num):
    for j in range(i):
        if point[j][1] < point[i][1]:
            result[i] = max(result[i], result[j] + 1)

print(num - max(result))