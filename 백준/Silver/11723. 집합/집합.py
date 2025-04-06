import sys
input = sys.stdin.readline

A = set()
num = int(input())
for _ in range(num):
    cmd = input().strip().split()
    if len(cmd) == 1: # all 또는 empty
        if cmd[0] == 'all':
            A = set(range(1, 21))
        else:
            A = set()
    else:
        x = int(cmd[1])
        if cmd[0] == 'add':
            A.add(x)
        elif cmd[0] == 'remove':
            A.discard(x)
        elif cmd[0] == 'check':
            if x in A:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            if x in A:
                A.discard(x)
            else:
                A.add(x)