import sys
input = sys.stdin.readline

def round_new(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

all_level = []
num = int(input())
if num:
    for _ in range(num):
        all_level.append(int(input()))
        
    cutting = round_new(num * 0.15) # 슬라이싱할 size 추출
    all_level.sort()
    if cutting > 0:
        new_level = all_level[cutting:num - cutting]
        print(round_new(sum(new_level)/len(new_level)))
    else:
        print(round_new(sum(all_level)/len(all_level)))
else:
    print(0)