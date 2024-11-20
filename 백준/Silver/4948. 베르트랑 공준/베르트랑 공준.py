def Is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime = []
for i in range(1, 2*123456):
    if Is_prime(i):
        prime.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in prime:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)