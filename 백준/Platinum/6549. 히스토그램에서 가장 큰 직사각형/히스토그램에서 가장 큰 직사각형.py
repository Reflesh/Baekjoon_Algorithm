import sys

def sol(Rec):
    Rec.append(0)  # 마지막 원소로 작은 값 0을 추가하여 스택이 비워지도록 도와줌
    stack = []
    max_area = 0

    for i in range(len(Rec)):
        while stack and Rec[stack[-1]] > Rec[i]: # 스택의 최상단 높이보다 작은 경우 max_area 갱신
            height = Rec[stack.pop()]
            if not stack:
                width = i  # 스택이 비어 있다면, 현재 막대는 0부터 i까지 확장 가능
            else:
                width = i - stack[-1] - 1  # 왼쪽의 낮은 막대 바로 오른쪽부터 현재 i-1까지 확장 가능
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

while True:
    Rec_ = list(map(int, sys.stdin.readline().split()))
    if Rec_[0] == 0:
        break
    Rec = Rec_[1:]
    print(sol(Rec))