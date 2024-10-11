n = int(input())
numbers = map(int, input().split())
prime_count = 0

for num in numbers:
    count = 0
    if num > 1:
        for t in range(2, num):
            if num % t == 0:
                count += 1
        if count == 0:
            prime_count += 1

print(prime_count)