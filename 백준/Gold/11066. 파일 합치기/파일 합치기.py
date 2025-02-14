import sys
input = sys.stdin.readline

case_num = int(input())
for _ in range(case_num):
    file_size = int(input())
    ls = [0]
    tmp = list(map(int, input().split()))
    ls.extend(tmp)
    # print(ls)
    
    sum = [0 for _ in range(file_size+1)]
    for i in range(file_size):
        sum[i+1] = sum[i] + ls[i+1] # 누적 합 구하기 
    # print(sum)
    
    sol = [[0 for _ in range(file_size+1)] for _ in range(file_size+1)]
    for i in range(1, file_size): # 구해야할 범위
        for start in range(1, file_size-i+1): # 합치는 범위의 시작 지점
            end = start + i # 합치는 범위의 끝 지점
            min_file = 1000000000 # 해당 범위(start ~ end)를 합치는데 필요한 최소 비용
            for k in range(start, end):
                min_file = min(min_file, sol[start][k] + sol[k+1][end])
                
            sol[start][end] = min_file + sum[end] - sum[start-1] # 최소 비용 갱신
                
    print(sol[1][file_size])