def mul(a, b): # 행렬 곱셈 수행 
    res = [[0] * 2 for _ in range(2)] # 결과 저장 
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD
    return res

def sol(x, n): # 행렬 거듭제곱 수행
    if n == 1:
        return x
    tmp = sol(x, n // 2)
    if n % 2: # n이 홀수인 경우
        return mul(mul(tmp, tmp), x)
    else: # n이 짝수인 경우 
        return mul(tmp, tmp)
    
MOD = 1000000007
num = int(input())
# 기본적인 피보나치 점화식:
#   | F(n)   | = | 1 1 | * | F(n-1) |
#   | F(n-1) |   | 1 0 |   | F(n-2) |
matrix = [[1, 1], [1, 0]]
result = sol(matrix, num)
print(result[0][1] % MOD)