while True:
    stack = []
    text = input()
    
    if text == '.':
        break
    
    for sentence in text:
        if sentence == '(' or sentence == '[':
            stack.append(sentence)
        elif sentence == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(sentence)
                break
        elif sentence == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(sentence)
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')