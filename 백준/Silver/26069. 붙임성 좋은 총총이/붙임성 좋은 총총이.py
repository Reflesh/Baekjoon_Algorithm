N = int(input())
dance = set()
dance.add('ChongChong')

for _ in range(N):
    person = input().split()
    if person[0] in dance:
        dance.add(person[1])
    elif person[1] in dance:
        dance.add(person[0])
        
print(len(dance))