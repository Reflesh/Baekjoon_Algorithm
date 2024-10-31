import sys

n = int(input())
num_list = []

for _ in range(n):
    s = int(sys.stdin.readline())
    num_list.append(s)
    
num_list.sort()

for i in range(n):
    print(num_list[i])