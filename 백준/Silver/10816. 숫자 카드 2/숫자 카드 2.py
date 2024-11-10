n = int(input())
Sanggeun_card = list(map(int, input().split()))
Sanggeun_dic = {}

for i in Sanggeun_card:
    if i in Sanggeun_dic:
        Sanggeun_dic[i] += 1
    else:
        Sanggeun_dic[i] = 1

m = int(input())
cmp_card = list(map(int, input().split()))

for i in cmp_card:
    if i in Sanggeun_dic:
        print(Sanggeun_dic[i], end = ' ')
    else:
        print(0, end = ' ')