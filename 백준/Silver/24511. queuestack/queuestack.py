import sys
from collections import deque

n = int(input())
queuestack = list(map(int, sys.stdin.readline().split()))
qs_element = list(map(int, sys.stdin.readline().split()))
m = int(input())
insert_element = list(map(int, sys.stdin.readline().split()))

flag = deque()

for i in range(n):
    if queuestack[i] == 0:
        flag.appendleft(qs_element[i])
        
for i in insert_element:
    flag.append(i)
    print(flag.popleft(), end = ' ')