import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
jew = []
for _ in range(n):
    jew_weight, jew_price = map(int, input().split())
    jew.append([jew_weight, jew_price])
jew.sort()
bag = []
for _ in range(k):
   bag.append(int(input()))
bag.sort()

j = 0
result = 0
heap = []
for i in bag:
    while j < n and jew[j][0] <= i:
        heapq.heappush(heap, -jew[j][1])
        j += 1
    if heap:
        result += -heapq.heappop(heap)
        
print(result)