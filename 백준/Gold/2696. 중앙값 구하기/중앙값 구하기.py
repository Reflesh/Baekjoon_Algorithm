import sys, heapq
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    size = int(input())
    result = [] # 중간값 저장
    left = [] # 중간값 이하의 숫자 저장(음수로 저장)
    right = [] # 중간값 초과의 숫자 저장
    cnt = 0
    for _ in range(size//10+1): # 10개씩 나누어 입력받기(문제조건)
        seq = list(map(int, input().split()))
        #print(seq)
        for num in seq:
            if cnt >= size:
                break

            if len(left) == len(right): # 힙 삽입 (크기 맞춰가며)
                heapq.heappush(left, -num)
            else:
                heapq.heappush(right, num)

            # 중간값이 left[0]에 위치하기 위해 swap
            if right and -left[0] > right[0]:
                l = -heapq.heappop(left)
                r = heapq.heappop(right)
                heapq.heappush(left, -r)
                heapq.heappush(right, l)

            cnt += 1
            if cnt % 2 == 1:  # 홀수 번째라면 중간값 저장
                result.append(-left[0])
        
    print(len(result))
    for num in range(0, len(result), 10):
        print(*result[num:num+10]) # 10개씩 출력