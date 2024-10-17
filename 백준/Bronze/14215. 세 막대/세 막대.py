a, b, c = map(int, input().split())
sum_side = a + b + c
if sum_side - max(a, b, c) > max(a, b, c):
    print(sum_side)
else:
    print(2 * (sum_side - max(a, b, c)) - 1)