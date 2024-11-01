n = list(map(int, input().strip()))
result = ''
n.sort(reverse = True)

for i in range(len(n)):
    result += str(n[i])

print(result)