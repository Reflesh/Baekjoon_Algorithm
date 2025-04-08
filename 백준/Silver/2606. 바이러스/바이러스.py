import sys
input = sys.stdin.readline

def dfs(n):
    global cnt
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            cnt += 1
            dfs(i)         

computer_num = int(input())
connection = int(input())
graph = [[] for i in range(computer_num+1)]
visited = [False] * (computer_num+1)
for _ in range(connection):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
#print(graph)
dfs(1)
print(cnt)