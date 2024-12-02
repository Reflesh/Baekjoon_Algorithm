import sys
from collections import deque

n = int(input())
balloon = deque(enumerate(map(int, sys.stdin.readline().split())))

for _ in range(n):
    idx, num = balloon.popleft()
    print(idx + 1, end = ' ')
    if num > 0:
        balloon.rotate(-(num - 1))
    else:
        balloon.rotate(-num)