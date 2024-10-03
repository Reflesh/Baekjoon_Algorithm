paper = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())

for _ in range(n):
    width, height = map(int, input().split())
    for i in range(width, width + 10):
        for j in range(height, height + 10):
            paper[i][j] = 1

area = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1
            
print(area)