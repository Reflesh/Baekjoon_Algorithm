T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    people = []
    for i in range(1, n + 1):
        people.append(i)
        
    for i in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]
    
    print(people[-1])