import math

A_num, A_den = map(int, input().split())
B_num, B_den = map(int, input().split())
result_num = A_num * B_den + B_num * A_den
result_den = A_den * B_den
gcd = math.gcd(result_num, result_den)

print(result_num // gcd, result_den // gcd)