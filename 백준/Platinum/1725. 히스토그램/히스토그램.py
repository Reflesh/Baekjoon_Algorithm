import sys
input = sys.stdin.readline

size = int(input())
Rec = [int(input()) for _ in range(size)]

Rec.append(0)  # 남아있는 모든 막대를 처리하기 위함
stack = []     # index 저장
max_area = 0   # 최대 넓이
for i in range(size+1):
    while stack and Rec[stack[-1]] > Rec[i]:  # 높이가 더 높은 경우
        height = Rec[stack.pop()]
        if not stack:   # 스택이 비어있는 경우
            width = i   # 현재 위치가 너비
        else:
            width = i - stack[-1] - 1  # 현재 index와 스택 최상단 index 사이의 거리 계산
        max_area = max(max_area, height * width) # 최대 넓이 갱신
    stack.append(i)  # index 저장

print(max_area)