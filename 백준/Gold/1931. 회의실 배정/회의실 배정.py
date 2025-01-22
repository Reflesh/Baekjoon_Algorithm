import sys

num = int(input())
time = []
for i in range(num):
    start_time, end_time = map(int, sys.stdin.readline().split())
    time.append((start_time, end_time))
        
time.sort(key=lambda x : (x[1], x[0]))
# print(time)
cnt = 1
fin = time[0][1]
for i in range(1, num):
    if time[i][0] >= fin:
        fin = time[i][1]
        cnt += 1
        
print(cnt)