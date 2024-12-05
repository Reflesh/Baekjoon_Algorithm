def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
    
n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))