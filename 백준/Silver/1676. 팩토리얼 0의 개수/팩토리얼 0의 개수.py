def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
    
N = int(input())
result = factorial(N)
digit = []
while result > 0: # 뒷숫자부터 digit리스트에 저장
    num = result % 10
    digit.append(num)
    result //= 10
    
cnt = 0
i = 0
while digit[i] == 0:
    i += 1
    cnt += 1
print(cnt)