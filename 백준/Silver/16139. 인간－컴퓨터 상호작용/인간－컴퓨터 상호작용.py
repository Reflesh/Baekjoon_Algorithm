import sys

letter = input()
num = int(input())
result = {}

# 등장하는 문자의 누적 합 딕셔너리 생성
for i, char in enumerate(letter):
    if char not in result:
        result[char] = [0] * len(letter)
    result[char][i] = 1
    
# 누적 합 계산
for char in result:
    for i in range(1, len(letter)):
        result[char][i] += result[char][i-1]

# 결과값 출력 
for _ in range(num):
    alpha, start_index, end_index = sys.stdin.readline().split()
    start_index, end_index = int(start_index), int(end_index)
    if alpha in result:
        if start_index:
            print(result[alpha][end_index] - result[alpha][start_index-1])
        else:
            print(result[alpha][end_index])
    else:
        print(0)