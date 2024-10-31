import sys

n = int(input())
counting = [0] * 10001

for _ in range(n):
    s = int(sys.stdin.readline())
    counting[s] += 1

for i in range(10001):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i)