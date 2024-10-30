n_list = []

for _ in range(5):
    n = int(input())
    n_list.append(n)
    
n_list.sort()
avg = sum(n_list) // 5
center = n_list[2]

print(avg)
print(center)