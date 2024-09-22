n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for _ in range(m):
    f, s = map(int, input().split())
    tmp = basket[s - 1]
    basket[s - 1] = basket[f - 1]
    basket[f - 1] = tmp
    
print(*basket, end = " ")