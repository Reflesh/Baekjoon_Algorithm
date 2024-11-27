n = int(input())
line = list(map(int, input().split()))
stack = []

turn = 1
for student in line:
    if student == turn:
        turn += 1
    else:
        stack.append(student)
    while len(stack) != 0 and stack[-1] == turn:
        stack.pop()
        turn += 1
        
if len(stack) == 0:
    print('Nice')
else:
    print('Sad')