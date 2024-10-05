n, b = map(int, input().split())
result = ''
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n:
    result += arr[n % b]
    n //= b
    
print(result[::-1])