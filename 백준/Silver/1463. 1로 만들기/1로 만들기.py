num = int(input())
result = {1:0}

def sol(n):
    if n in result.keys():
        return result[n]
    if n % 3 == 0 and n % 2 == 0:
        result[n] = min(sol(n//3) + 1, sol(n//2) + 1)
    elif n % 3 == 0:
        result[n] = min(sol(n//3) + 1, sol(n-1) + 1)
    elif n % 2 == 0:
        result[n] = min(sol(n//2) + 1, sol(n-1) + 1)
    else:
        result[n] = sol(n-1) + 1
    return result[n]

print(sol(num))