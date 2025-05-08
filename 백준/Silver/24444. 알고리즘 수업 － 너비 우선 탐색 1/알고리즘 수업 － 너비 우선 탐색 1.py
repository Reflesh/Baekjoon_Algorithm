import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt

    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if visited[neighbor] == 0:
                cnt += 1
                visited[neighbor] = cnt
                queue.append(neighbor)

vertex, edge, starting = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
visited = [0] * (vertex+1)
cnt = 1

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for g in graph:
    g.sort()
    
bfs(starting)

for i in range(1, vertex+1):
    print(visited[i])