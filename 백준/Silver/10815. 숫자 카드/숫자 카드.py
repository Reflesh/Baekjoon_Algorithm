n = int(input())
Sanggeun_card = list(map(int, input().split()))
m = int(input())
cmp_card = list(map(int, input().split()))
dic = {}

for i in Sanggeun_card:
    dic[i] = 0

for i in cmp_card:
    if i in dic:
        print(1, end = ' ')
    else:
        print(0, end = ' ')