n = int(input())

for _ in range(n):
    prime = int(input())   
    while True:
        if prime == 0 or prime == 1:
            Is_prime = False    
        else:
            Is_prime = True
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                Is_prime = False
                break
        if Is_prime:
            print(prime)
            break
        else:
            prime += 1