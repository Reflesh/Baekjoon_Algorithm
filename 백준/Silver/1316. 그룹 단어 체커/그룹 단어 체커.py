count = int(input())
group = 0

for i in range(count):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            continue
        elif word[j] in word[j + 1:]:
            group += 1
            break
print(count - group)