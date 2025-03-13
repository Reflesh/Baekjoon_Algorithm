import sys
input = sys.stdin.readline

num_people = int(input().strip())
heights = [int(input().strip()) for _ in range(num_people)]

stack = []  # (키, 같은 키 개수) 저장
total_views = 0
for height in heights:
    count = 1  # 현재 키와 동일한 사람의 수수
    # 스택의 top이 현재 키보다 작거나 같으면 pop
    while stack and stack[-1][0] <= height:
        popped_height, popped_count = stack.pop()
        total_views += popped_count  # pop된 사람들은 현재 사람을 볼 수 있음
        if popped_height == height:
            count += popped_count  # 같은 키면 개수 증가
            
    if stack: # 스택이 비어있지 않으면 한 명은 추가적으로 볼 수 있음
        total_views += 1

    stack.append((height, count)) # 현재 키와 개수를 스택에 push

print(total_views)