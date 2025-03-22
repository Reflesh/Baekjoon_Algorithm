import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    global cnt
    visited[idx] = cnt # 방문 순서 기록
    graph[idx].sort(reverse=True) # 내림차순으로 정렬
    for i in graph[idx]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    
vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
visited = [0] * (vertex+1)
cnt = 1

for _ in range(edge): # 양방향 간선 정보 입력
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(start)

for i in range(1, vertex+1):
    print(visited[i])