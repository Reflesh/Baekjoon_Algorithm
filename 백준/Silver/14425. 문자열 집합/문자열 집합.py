n, m = map(int, input().split())
char_list = []
cmp_list = []
dic = {}

for i in range(n):
    ch = input()
    char_list.append(ch)
    
for i in range(m):
    cmp_ch = input()
    cmp_list.append(cmp_ch)
    
for i in char_list:
    dic[i] = 0
    
cnt = 0
for i in cmp_list:
    if i in dic:
        cnt += 1

print(cnt)