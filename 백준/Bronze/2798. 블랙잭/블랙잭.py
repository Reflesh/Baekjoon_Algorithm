count, number = map(int, input().split())
card_list = list(map(int, input().split()))
max_list = []

for i in range(len(card_list) - 2):
    for j in range(i + 1, len(card_list) - 1):
        for k in range(j + 1, len(card_list)):
            card_sum = card_list[i] + card_list[j] + card_list[k]
            if card_sum <= number:
                max_list.append(card_sum)

#print(card_list)
#print(max_list)             
print(max(max_list))