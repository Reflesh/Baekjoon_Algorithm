num = int(input())
wine = []

for _ in range(num):
    wine.append(int(input()))
    
if num == 1:
    print(wine[0])
elif num == 2:
    print(sum(wine))
else:
    result = [0] * num
    result[0] = wine[0]
    result[1] = result[0] + wine[1]
    result[2] = max(wine[1] + wine[2], wine[0] + wine[2], result[1])
    
    for i in range(3, num):
        result[i] = max(result[i-2] + wine[i], result[i-3] + wine[i-1] + wine[i], result[i-1])
        
    print(result[-1])