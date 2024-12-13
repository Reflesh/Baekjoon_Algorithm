N = int(input())

for i in range(N):
    start, end = map(int, input().split())
    sum = (end - start + 1) * (start + end) // 2
    print(f'Scenario #{i+1}:')
    print(sum)
    print()