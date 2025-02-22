import sys
input = sys.stdin.readline

size = int(input())
NGE = list(map(int, input().split()))

stack = []             # index 저장
result = [-1] * size   # 결과값 저장
for i in range(size):
    while stack and NGE[stack[-1]] < NGE[i]:
        result[stack.pop()] = NGE[i] # 현재 값보다 작은 값을 찾은 경우 값 저장
    stack.append(i)                  # 다음 연산을 위해 append()
    
print(*result)