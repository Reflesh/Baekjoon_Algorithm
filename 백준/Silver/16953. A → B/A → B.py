import sys
input = sys.stdin.readline

first_num, second_num = map(int, input().split())
cnt = 0
while first_num < second_num:
    if second_num % 10 == 1:
        second_num //= 10
        cnt += 1
        #print(second_num)
    elif second_num % 2 == 0:
        second_num //= 2
        cnt += 1
        #print(second_num)
    else:
        break

if first_num == second_num:
    print(cnt+1)
else:
    print(-1)