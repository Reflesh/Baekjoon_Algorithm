formula = input()
number = []
operator = []
temp_num = ''

for char in formula: # 부호와 숫자 분리 
    if char.isdigit():
        temp_num += char
    else:
        if temp_num:
            number.append(int(temp_num))
            temp_num = ''
        operator.append(char)

if temp_num: # 마지막 숫자 추가
    number.append(int(temp_num))

tmp = 0
result = number[0]
sub = False # '-' 연산자의 상태 저장
for i in range(len(operator)):
    if operator[i] == '-':
        if sub:
            result -= tmp
        else:
            result += tmp
        # '-' 연산자를 만나면 이후의 숫자를 모두 묶어서 뺄셈 연산 수행
        tmp = number[i+1] 
        sub = True
    else:
        if sub:
            tmp += number[i+1]
        else:
            result += number[i+1]
            
if sub: # 마지막 tmp 계산
    result -= tmp
    
print(result)