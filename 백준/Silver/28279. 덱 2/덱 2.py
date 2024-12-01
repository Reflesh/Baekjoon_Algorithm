import sys
from collections import deque

n = int(input())
deq = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1':
        deq.appendleft(cmd[1])
    elif cmd[0] == '2':
        deq.append(cmd[1])
    elif cmd[0] == '3':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == '4':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == '5':
        print(len(deq))
    elif cmd[0] == '6':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == '7':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == '8':
        if deq:
            print(deq[-1])
        else:
            print(-1)