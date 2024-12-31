def fib(n):
    global cnt_fib
    if n == 1 or n == 2:
        cnt_fib += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global cnt_fibonacci
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        cnt_fibonacci += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
    
N = int(input())
f = [0] * (N + 1)
cnt_fib, cnt_fibonacci = 0, 0
fib(N)
fibonacci(N)
print(cnt_fib, cnt_fibonacci)