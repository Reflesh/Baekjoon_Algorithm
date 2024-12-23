from itertools import permutations

num, length = map(int, input().split())
sequences = list(permutations(range(1, num + 1), length))

for i in range(len(sequences)):
    print(*sequences[i])