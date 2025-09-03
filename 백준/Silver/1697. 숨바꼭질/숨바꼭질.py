import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == sibling:
            return distance[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)
                
MAX = 100000
distance = [0] * (MAX + 1)
subin, sibling = map(int, input().split())
print(bfs(subin))