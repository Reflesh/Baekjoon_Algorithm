def pow_(A, B):
    if B == 0:
        return 1
    if B % 2 == 1: # 홀수인 경우
        return (pow_(A, B // 2) ** 2 * A) % P
    else:          # 짝수인 경우
        return (pow_(A, B // 2) ** 2) % P

num, K = map(int, input().split())

factorial = [1 for _ in range(num+1)]

P = 1000000007 # 문제 조건
for i in range(2, num + 1):
    factorial[i] = factorial[i-1] * i % P

numerator = factorial[num]
denominator = (factorial[num-K] * factorial[K]) % P

print((numerator % P) * (pow_(denominator, P-2) % P) % P)