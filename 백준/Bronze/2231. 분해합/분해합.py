n = int(input())

for i in range(1, n + 1):
    num = i
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    if result + i == n:
        print(i)
        break
    if i == n:
        print(0)