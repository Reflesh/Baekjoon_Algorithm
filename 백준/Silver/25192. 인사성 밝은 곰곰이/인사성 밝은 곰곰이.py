import sys

N = int(input())
cnt = 0
user = {}

for _ in range(N):
    chat = sys.stdin.readline().strip()
    
    if chat == 'ENTER':
        cnt += len(user)
        user = {}
    else:
        if chat not in user:
            user[chat] = True
            
if user:
    cnt += len(user)

print(cnt)