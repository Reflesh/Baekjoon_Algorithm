import sys
input = sys.stdin.readline

Len = int(input())
Eng = list(input().strip())
#print(Eng)
hash = 0
for idx, s in enumerate(Eng):
    num = ord(s) - 96
    hash += num * (31 ** idx)
    
print(hash % 1234567891)