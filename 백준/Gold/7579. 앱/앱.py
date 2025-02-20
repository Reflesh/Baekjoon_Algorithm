import sys
input = sys.stdin.readline

num, memory = map(int, input().split())
App = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost)+1) for _ in range(num+1)]

result = sum(cost)
for idx in range(1, num+1):
    for cst in range(sum(cost)+1):
        if cst < cost[idx]:                 # cost가 충분하지 않은 경우
            dp[idx][cst] = dp[idx-1][cst]   # 그대로 값 유지
        else:                               # 값 갱신
            dp[idx][cst] = max(dp[idx-1][cst], App[idx] + dp[idx-1][cst-cost[idx]])
        if dp[idx][cst] >= memory:          # 필요한 메모리에 도달한 경우
            result = min(result, cst)       # 더 작은 값으로 갱신
            
print(result)