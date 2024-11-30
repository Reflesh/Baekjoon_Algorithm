from collections import deque

capacity, rm_num = map(int, input().split())
circle = deque()

for i in range(1, capacity + 1):
    circle.append(i)

print('<', end = '')
for i in range(capacity):
    circle.rotate(-(rm_num- 1))
    print(circle.popleft(), end = '')
    if i != capacity - 1:
        print(', ', end = '')

print('>')