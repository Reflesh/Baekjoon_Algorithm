import sys
input = sys.stdin.readline

def binary_search(start, end, target, res):
    while start < end:
        mid = (start + end) // 2
        if res[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

size = int(input()) 
A = list(map(int, input().split()))

result = [A[0]]
cnt = 1
for i in range(size):
    if result[cnt-1] < A[i]:
        result.append(A[i])
        cnt += 1
    else:
        idx = binary_search(0, cnt - 1, A[i], result)
        result[idx] = A[i]
        
print(cnt)