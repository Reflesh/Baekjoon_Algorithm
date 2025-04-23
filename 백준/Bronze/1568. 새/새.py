import sys
input = sys.stdin.readline

bird_num = int(input())
sing_num = 1
time = 0
while bird_num > 0:
    if bird_num < sing_num: # 현재 나무에 앉아있는 새의 수가 지금 불러야하는 수보다 작은 경우
        sing_num = 1 # 1로 초기화
    bird_num -= sing_num
    sing_num += 1
    time += 1
        
print(time)