N = int(input())
result = [0, 1, 2]

for i in range(3, N+1):
    result.append((result[i-1] + result[i-2]) % 15746)

print(result[N] % 15746)