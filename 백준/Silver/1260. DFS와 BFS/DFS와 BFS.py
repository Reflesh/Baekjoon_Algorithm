import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global cnt_bfs
    queue = deque([start])
    visited_bfs[start] = cnt_bfs

    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if visited_bfs[neighbor] == 0:
                cnt_bfs += 1
                visited_bfs[neighbor] = cnt_bfs
                queue.append(neighbor)

def dfs(idx):
    global cnt_dfs
    visited_dfs[idx] = cnt_dfs
    graph[idx].sort()
    for i in graph[idx]:
        if visited_dfs[i] == 0:
            cnt_dfs += 1
            dfs(i)

vertex, edge, starting = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
visited_bfs = [0] * (vertex+1)
visited_dfs = [0] * (vertex+1)
cnt_bfs = 1
cnt_dfs = 1

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for g in graph:
    g.sort()

dfs(starting)    
bfs(starting)

Answer_dfs = [0] * (vertex+1)
Answer_bfs = [0] * (vertex+1)
for i in range(1, vertex+1):
    Answer_dfs[visited_dfs[i]] = i
for i in range(1, vertex+1):
    Answer_bfs[visited_bfs[i]] = i
    
for i in range(1, vertex+1):
    if Answer_dfs[i]:
        print(Answer_dfs[i], end=' ')
print()
for i in range(1, vertex+1):
    if Answer_bfs[i]:
        print(Answer_bfs[i], end=' ')