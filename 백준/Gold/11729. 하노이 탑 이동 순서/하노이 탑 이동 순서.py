def hanoi_tower(n, fr, tmp, to):
    global cnt
    global result_from
    global result_to
    if n == 1:
        result_from.append(fr)
        result_to.append(to)
        cnt += 1
    else:
        hanoi_tower(n-1, fr, to, tmp)
        result_from.append(fr)
        result_to.append(to)
        cnt += 1
        hanoi_tower(n-1, tmp, fr, to)
    
N = int(input())
cnt = 0
result_from = []
result_to = []
hanoi_tower(N, 1, 2, 3)
print(cnt)
for i in range(cnt):
    print(result_from[i], result_to[i])