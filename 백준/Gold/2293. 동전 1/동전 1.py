import sys
input = sys.stdin.readline

num, coin = map(int, input().split())
cost = []
for _ in range(num):
    cost.append(int(input()))
    
dp = [0 for _ in range(coin + 1)]
dp[0] = 1
for cn in cost:
    for k in range(cn, coin + 1):
        dp[k] += dp[k-cn]

print(dp[coin])