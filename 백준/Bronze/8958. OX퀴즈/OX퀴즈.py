import sys
input = sys.stdin.readline

size = int(input())

for _ in range(size):
    quiz = list(input().strip())
    score = 0
    cnt = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
            
    print(score)