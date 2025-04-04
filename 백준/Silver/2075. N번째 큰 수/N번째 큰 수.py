import sys, heapq
input = sys.stdin.readline

size = int(input())
graph = []
graph_row = list(map(int, input().split()))
for num in graph_row:
    heapq.heappush(graph, num)
    
#print(graph)
for _ in range(size-1):
    graph_row = list(map(int, input().split()))
    for num in graph_row:
        if graph[0] < num:
            heapq.heappush(graph, num)
            heapq.heappop(graph)
            
print(graph[0])