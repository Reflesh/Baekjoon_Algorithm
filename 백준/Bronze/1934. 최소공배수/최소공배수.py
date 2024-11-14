import math

number = int(input())

for _ in range(number):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    result = A * B // gcd
    print(result)