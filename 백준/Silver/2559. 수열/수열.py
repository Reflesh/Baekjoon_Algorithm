num, cnt = map(int, input().split())
ls = list(map(int, input().split()))

result = []
result.append(sum(ls[0:cnt]))

for i in range(num - cnt):
    result.append(result[i] + ls[i + cnt] - ls[i])
    
print(max(result))