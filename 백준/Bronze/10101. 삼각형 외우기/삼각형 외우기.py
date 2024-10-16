angle_list = []

for _ in range(3):
    n = int(input())
    angle_list.append(n)
    
if angle_list.count(60) == 3:
    print('Equilateral')
elif sum(angle_list) == 180 and len(set(angle_list)) == 2:
    print('Isosceles')
elif sum(angle_list) == 180 and len(set(angle_list)) == 3:
    print('Scalene')
else:
    print('Error')