import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    size = int(input())
    dp = [0] * (size+1)
    for i in range(1, size+1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[size])