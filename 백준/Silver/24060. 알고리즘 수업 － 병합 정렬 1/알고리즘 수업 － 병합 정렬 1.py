def merge_sort(A, p, r, save_count, cnt):
    result = -1
    if p < r:
        q = (p + r) // 2
        result, cnt = merge_sort(A, p, q, save_count, cnt)
        if result != -1:  # 이미 결과를 찾은 경우 조기 종료
            return result, cnt
        result, cnt = merge_sort(A, q + 1, r, save_count, cnt)
        if result != -1:  # 이미 결과를 찾은 경우 조기 종료
            return result, cnt
        result, cnt = merge(A, p, q, r, save_count, cnt)
    return result, cnt

def merge(A, p, q, r, save_count, cnt):
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    i = p
    t = 0 # 의사코드에서는 t가 1로 시작하지만 해당 코드는 배열에 append로 삽입하므로 0부터 시작
    result = -1
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == save_count:
            result = A[i]
            break
        i += 1
        t += 1
    return result, cnt

size, save_count = map(int, input().split())
array = list(map(int, input().split()))
result, _ = merge_sort(array, 0, size - 1, save_count, 0)
print(result)