function_a1, function_a2 = map(int, input().split())
c = int(input())
n = int(input())

if (function_a1 * n + function_a2 <= c * n) and function_a1 <= c:
    print(1)
else:
    print(0)