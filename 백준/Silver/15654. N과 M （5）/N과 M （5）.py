from itertools import permutations

n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
for i in permutations(l,m):
    for t in i:
        print(t,end = " ")
    print()