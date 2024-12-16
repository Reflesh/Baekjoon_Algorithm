A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result = list(str(result))

for i in range(10):
    print(result.count(str(i)))