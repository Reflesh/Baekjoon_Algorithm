import sys
input = sys.stdin.readline

num = int(input())
shirt_size = list(map(int, input().split()))
pack = list(map(int, input().split()))
result = 0
for T in shirt_size:
    if T % pack[0] == 0:
        result += T // pack[0]
    else:
        tmp = T // pack[0] + 1
        result += tmp
    #print(result)
    
print(result)
print(num//pack[1], num%pack[1])