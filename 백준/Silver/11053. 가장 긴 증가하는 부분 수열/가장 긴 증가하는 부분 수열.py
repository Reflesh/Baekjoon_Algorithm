from bisect import bisect_left

length = int(input())
seq = (list(map(int, input().split())))

result = [0] # 최대 길이
min_seq = [0] # 작은 값 저장

for i in range(length):
    if seq[i] > min_seq[-1]:
        min_seq.append(seq[i])
        result.append(result[-1] + 1)
    else:
        pos = bisect_left(min_seq, seq[i])
        min_seq[pos] = seq[i]
        
print(len(min_seq) - 1)