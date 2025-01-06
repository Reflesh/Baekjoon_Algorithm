n = int(input())
stairs = []

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[0])
elif n == 2:
    print(sum(stairs))
else:
    result = [0] * n
    result[0] = stairs[0]
    result[1] = result[0] + stairs[1]
    result[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        result[i] = max(result[i-3] + stairs[i-1] + stairs[i], result[i-2] + stairs[i])
        
    print(result[-1])