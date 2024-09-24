n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for t in range(n - 1, 0, -1):
    print(' ' * (n - t) + '*' * (2 * t - 1))