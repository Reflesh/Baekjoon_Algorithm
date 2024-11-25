import sys

stack = []
n = int(input())

for _ in range(n):
    String = list(sys.stdin.readline().strip())
    balanced = True
    for s in String:  
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                balanced = False
                break
    if balanced and not stack:
        print('YES')
    else:
        print('NO')
    stack.clear()