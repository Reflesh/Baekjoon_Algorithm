import sys
import heapq
input = sys.stdin.readline

cnt = int(input())
heap = []
for _ in range(cnt):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)