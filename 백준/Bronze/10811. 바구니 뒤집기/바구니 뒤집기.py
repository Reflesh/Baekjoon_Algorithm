n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
# 2 1 4 3 5
# 3 4 1 2 5
for _ in range(m):
    s, t = map(int, input().split())
    tmp = basket[s-1:t]
    tmp.reverse()
    basket[s-1:t] = tmp
    
print(*basket, end = ' ')