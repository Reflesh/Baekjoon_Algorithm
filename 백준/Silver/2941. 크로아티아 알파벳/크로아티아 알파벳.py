check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ch = input()
cnt = 0

for i in check:
    cnt += ch.count(i)
    
print(len(ch) - cnt)