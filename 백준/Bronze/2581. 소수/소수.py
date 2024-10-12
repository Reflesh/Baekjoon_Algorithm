m = int(input())
n = int(input())
prime_ls = []

for i in range(m, n + 1):
    if i <= 1:
        continue
    Is_Prime = True
    for t in range(2, int(i ** 0.5) + 1): # 제곱근까지만 검사해도 충분
        if i % t == 0:
            Is_Prime = False
            break
    if Is_Prime:
        prime_ls.append(i)
    
if prime_ls:
    # print(prime_ls) test
    print(sum(prime_ls))
    print(min(prime_ls))
else:
    print(-1)