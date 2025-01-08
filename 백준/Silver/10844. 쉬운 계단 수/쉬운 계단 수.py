num = int(input())

def sol(n):
    result = [[0] * 10 for _ in range(n + 1)]
    
    for i in range(1, 10):
        result[1][i] = 1
        
    for i in range(2, n + 1):
        for j in range(10):
            if j > 0:
                result[i][j] += result[i - 1][j - 1]
            if j < 9:
                result[i][j] += result[i - 1][j + 1]
        
    return sum(result[n])

print(sol(num) % 1000000000)
