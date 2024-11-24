import sys

diary = []
n = int(input())

for _ in range(n):
    money = int(sys.stdin.readline())
    if money == 0:
        diary.pop()
    else:
        diary.append(money)
        
print(sum(diary))