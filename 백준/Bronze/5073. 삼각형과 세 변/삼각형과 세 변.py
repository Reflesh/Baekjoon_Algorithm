while True:
    side_list = list(map(int, input().split()))
    if sum(side_list) == 0:
        break
    # 가장 긴 변의 길이가 나머지 두 변의 길이보다 길다면 삼각형의 조건을 만족하지 못함
    if sum(side_list) - max(side_list) <= max(side_list): 
        print('Invalid')
    elif len(set(side_list)) == 1:
        print('Equilateral')
    elif len(set(side_list)) == 2:
        print('Isosceles')
    else:
        print('Scalene')