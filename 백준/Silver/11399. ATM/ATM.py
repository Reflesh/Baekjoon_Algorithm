num = int(input())
time = list(map(int, input().split()))
time.sort()

result = [time[0]]
for i in range(1, num):
    result.append(result[i-1] + time[i])
    
print(sum(result))