def Is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

min, max = map(int, input().split())

for i in range(min, max + 1):
    if Is_prime(i):
        print(i)