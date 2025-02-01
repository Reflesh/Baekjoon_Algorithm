def mul(a, b): # 행렬 곱 구하는 함수
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += a[i][k] * b[k][j] % 1000
    return res

def sol(x, n): # 행렬 거듭제곱 구하는 함수
    if n == 1:
        return x
    tmp = sol(x, n // 2)
    if n % 2: # n이 홀수인 경우
        return mul(mul(tmp, tmp), x)
    else: # n이 짝수인 경우 
        return mul(tmp, tmp)
    
A = []
size, pow_num = map(int, input().split())
for _ in range(size):
    A.append(list(map(int, input().split())))
    
result = sol(A, pow_num)
for i in range(size): 
    for j in range(size):
        result[i][j] = result[i][j] % 1000 # 문제 조건
        
for i in result:
    print(*i)