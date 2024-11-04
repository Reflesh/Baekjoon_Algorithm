n = int(input())
person_info = []

for i in range(n):
    age, name = input().split()
    person_info.append((int(age), name))

# print(person_info)
person_info.sort(key = lambda x: x[0])

for i in range(n):
    print(person_info[i][0], person_info[i][1])