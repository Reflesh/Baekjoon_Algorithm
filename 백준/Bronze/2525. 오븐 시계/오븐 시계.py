h, m  = map(int, input().split())
c = int(input())
add_hour = 0
if(m+c>=60):
    add_hour=(m+c)//60
    real_min = m+c-add_hour*60
else :
    real_min = m+c


if(h+add_hour>23):
    real_hour = h+add_hour-24
else : 
    real_hour = h+add_hour 

print(f"{int(real_hour)} {int(real_min)}")