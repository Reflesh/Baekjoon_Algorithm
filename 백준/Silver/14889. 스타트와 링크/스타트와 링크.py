def solve(n, idx, start_team):
    global result
    if n == N//2:
        link_team = []
        for i in range(N):
            if i not in start_team:
                link_team.append(i)
                
        start_score, link_score = 0, 0
        for i in start_team:
            for j in start_team:
                start_score += ability[i][j]
        for i in link_team:
            for j in link_team:
                link_score += ability[i][j]
                
        result = min(result, abs(start_score - link_score))
        return
    
    for i in range(idx, N):
        solve(n + 1, i + 1, start_team + [i])
        

N = int(input())
ability = []
for _ in range(N):
    soccer = list(map(int, input().split()))
    ability.append(soccer)
    
result = 1000000

solve(0, 0, [])
print(result)