n, m = map(int, input().split())
unheard_people = set() 
unseen_people = set()

for _ in range(n):
    person = input()
    unheard_people.add(person)
    
for _ in range(m):
    person = input()
    unseen_people.add(person)
    
name_list = list(unseen_people & unheard_people)
name_list.sort()

print(len(name_list))
print('\n'.join(name_list))