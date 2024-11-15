import math

A, B = map(int, input().split())
gcd = math.gcd(A, B)
result = A * B // gcd
print(result)