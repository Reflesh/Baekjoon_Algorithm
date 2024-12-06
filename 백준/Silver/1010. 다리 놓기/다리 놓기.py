def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
    
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))