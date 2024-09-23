chess = [1, 1, 2, 2, 2, 8]
storage = [] * 6

num = input()
n = list(map(int, num.split()))
storage.extend(n)

for i in range(6):
    storage[i] = chess[i] - storage[i]
    
print(*storage)