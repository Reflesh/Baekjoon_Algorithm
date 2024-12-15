asc = [1, 2, 3, 4, 5, 6, 7, 8]
sound = list(map(int, input().split()))

if sound == asc:
    print('ascending')
elif sound == sorted(asc, reverse=True):
    print('descending')
else:
    print('mixed')