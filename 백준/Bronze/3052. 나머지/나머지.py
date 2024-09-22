mod_list = []
for i in range(10):
    d = int(input())
    d %= 42
    count = 0
    for j in range(len(mod_list)):
        if mod_list[j] == d:
            count += 1
            break
    if count == 0:
        mod_list.append(d)

print(len(mod_list))