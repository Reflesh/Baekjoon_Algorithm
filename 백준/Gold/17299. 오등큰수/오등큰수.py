import sys
input = sys.stdin.readline

size = int(input())
NGF = list(input().split())

count_NGF = {}
for num in NGF:  # 각 숫자의 등장 횟수 계산
    if num in count_NGF:
        count_NGF[num] += 1
    else:
        count_NGF[num] = 1

new_NGF = [count_NGF[num] for num in NGF]

stack = []
result = [-1] * size
for i in range(size):
    while stack and new_NGF[stack[-1]] < new_NGF[i]:
        result[stack.pop()] = NGF[i]
    stack.append(i)
    
print(*result)