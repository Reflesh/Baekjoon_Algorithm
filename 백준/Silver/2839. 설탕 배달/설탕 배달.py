n = int(input())
bag_3 = 0 # 3kg 봉지 수
possible_bag = []

while n >= 3 * bag_3:
    height = n - 3 * bag_3
    if height % 5 == 0:
        bag_5 = height // 5
        bag_5 += bag_3
        possible_bag.append(bag_5)
    bag_3 += 1

if len(possible_bag) == 0:
    print(-1)
else:
    print(min(possible_bag))