import sys

prime = [False] * 2 + [True] * 999999

for i in range(2, 1000001):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            prime[j] = False
            
T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    n = int(input())
    for i in range(2, n//2 + 1):
        if prime[i] and prime[n - i]:
            cnt += 1
    print(cnt)