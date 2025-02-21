import sys
input = sys.stdin.readline

text = input().strip()
Explosion = input().strip()

stack = []
for ch in text:
    stack.append(ch)
    if stack[-len(Explosion):] == list(Explosion):
        for _ in range(len(Explosion)):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print('FRULA')