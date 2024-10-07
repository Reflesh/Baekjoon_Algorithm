n = int(input())
room = 6
count = 0

while n > 0:
    if count == 0:
        n -= 1
        count += 1
    else:
        n -= room
        room += 6
        count += 1
        
print(count)