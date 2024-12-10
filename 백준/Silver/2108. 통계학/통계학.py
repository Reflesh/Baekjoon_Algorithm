import sys

N = int(input())
num_list = []
num_dic = {}

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)
    if num not in num_dic: # 최빈값 확인을 위한 딕셔너리
        num_dic[num] = 1
    else:
        num_dic[num] += 1
        
avg = sum(num_list) / len(num_list) # 평균 구하기
num_list.sort() # 리스트 정렬
# 중앙값 구하기
if len(num_list) % 2 == 0:  
    center = (num_list[len(num_list)//2] + num_list[len(num_list)//2 - 1]) / 2
else:
    center = num_list[len(num_list)//2]
# 최빈값 구하기
max_freq = max(num_dic.values())
num_freq = []
for key, val in num_dic.items():
    if val == max_freq:
        num_freq.append(key)
num_freq.sort()
if len(num_freq) != 1: # 여러 개일 경우 두 번째로 작은 값
    freq = num_freq[1]
else:
    freq = num_freq[0]

print(round(avg)) # 반올림
print(center) # 중앙값
print(freq) # 최빈값
print(max(num_list) - min(num_list)) # 범위