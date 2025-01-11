from bisect import bisect_left

length = int(input())
seq = (list(map(int, input().split())))

result_min = [0] * length # 최대 길이
min_seq = [] # 작은 값 저장

# 증가하는 부분
for i in range(length):
    pos = bisect_left(min_seq, seq[i])
    if pos == len(min_seq):
        min_seq.append(seq[i])
    else:
        min_seq[pos] = seq[i]
    result_min[i] = pos + 1
        
result_max = [0] * length
max_seq = [] # 큰 값 저장

# 감소하는 부분
for i in range(length - 1, -1, -1):  # 뒤에서부터 탐색
    pos = bisect_left(max_seq, seq[i])
    if pos == len(max_seq):
        max_seq.append(seq[i])
    else:
        max_seq[pos] = seq[i]
    result_max[i] = pos + 1
        
Answer = 0
for i in range(length):
    Answer = max(Answer, result_min[i] + result_max[i] - 1)

print(Answer)