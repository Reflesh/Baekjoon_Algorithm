num, div = map(int, input().split())
ls = list(map(int, input().split()))
remainder = [0] * div # 나머지값 저장

prefix_sum = 0
for i in range(num):
    prefix_sum += ls[i]
    remainder[prefix_sum % div] += 1

result = remainder[0] # 나머지가 0이 되는 경우의 수
for i in remainder:
    result += i * (i-1) // 2
    
print(result)