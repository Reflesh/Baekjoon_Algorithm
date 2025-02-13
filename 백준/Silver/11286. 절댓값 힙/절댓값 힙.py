import sys
import heapq
input = sys.stdin.readline

cnt = int(input())
max_heap = [] # 음수 절댓값 저장
min_heap = [] # 양수 절댓값 저장
for _ in range(cnt):
    x = int(input())
    if x == 0: # 결과값 출력
        if min_heap:
            if max_heap: # 최소힙과 최대힙이 둘 다 존재할 때
                if min_heap[0] < max_heap[0]:
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else: # 최소힙만 존재할 때 
                print(heapq.heappop(min_heap))
        elif max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    elif x > 0: # 양수일때
        heapq.heappush(min_heap, x)
    elif x < 0: # 음수일때
        heapq.heappush(max_heap, -x) 
