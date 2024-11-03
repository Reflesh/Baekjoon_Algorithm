n = int(input())
word_list = []

for i in range(n):
    word = input()
    word_list.append(word)
    
new_word = list(set(word_list))
new_word.sort(key = lambda x: (len(x), x))

for word in new_word:
    print(word)