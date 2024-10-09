up, down, height = map(int, input().split())
day = (height - down) / (up - down)

if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)