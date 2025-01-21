kind, money = map(int, input().split())
coin = []

for _ in range(kind):
    coin.append(int(input()))
    
cnt = 0
index = kind - 1
while money > 0:
    if coin[index] <= money:
        cnt += money // coin[index]
        money %= coin[index]
    else:
        index -= 1
        
print(cnt)