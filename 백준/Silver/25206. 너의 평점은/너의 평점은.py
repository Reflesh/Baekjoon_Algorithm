grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
credit = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
sum_credit = 0
sum_grade = 0

for _ in range(20):
    name, c, g = input().split()
    c = float(c)
    if g != 'P':
        sum_credit += c
        sum_grade += c * credit[grade.index(g)]
        
print(sum_grade / sum_credit)