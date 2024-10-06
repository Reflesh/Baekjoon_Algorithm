n = int(input())
point = 2 # 한 줄에 존재하는 점의 개수

for _ in range(n):
    point += (point - 1)
    
print(point ** 2)