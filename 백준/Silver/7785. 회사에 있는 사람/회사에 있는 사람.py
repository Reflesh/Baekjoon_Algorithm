n = int(input())
staff_in = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        staff_in[name] = i
    if status == 'leave':
        del staff_in[name]
        
staff_in_list = list(staff_in)
staff_in_list.sort(reverse = True)

for i in staff_in_list:
    print(i)