import math

first, second = map(int, input().split())
result = math.gcd(first, second)
print(result)
print(first * second // result)