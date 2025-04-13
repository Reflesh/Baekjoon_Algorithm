import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    wear_num = int(input())
    wear = {}
    for _ in range(wear_num):
        name, wear_type = input().split()
        if wear_type in wear:
            wear[wear_type].append(name)
        else:
            wear[wear_type] = [name]
            
    cnt = 1
    for i in wear:
        cnt *= (len(wear[i]) + 1)
    print(cnt-1)