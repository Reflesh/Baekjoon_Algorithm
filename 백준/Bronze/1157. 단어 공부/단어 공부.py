ch = input().upper()
test = {}

for i in ch:
    if i in test:
        test[i] += 1
    else:
        test[i] = 1
        
most_char = None
count = 0
max_confirm = False

for i, cnt in test.items():
    if cnt > count:
        most_char = i
        count = cnt
        max_confirm = False
    elif cnt == count:
        max_confirm = True
        
if max_confirm:
    print('?')
else:
    print(most_char)