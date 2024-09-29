sum_credit = 0
sum_grade = 0

for i in range(20):
    name, credit, grade = input().split()
    float_cd = float(credit)
    if grade == 'A+':
        sum_grade += float_cd * 4.5 
        sum_credit += float_cd
    elif grade == 'A0':
        sum_grade += float_cd * 4.0
        sum_credit += float_cd
    elif grade == 'B+':
        sum_grade += float_cd * 3.5
        sum_credit += float_cd
    elif grade == 'B0':
        sum_grade += float_cd * 3.0
        sum_credit += float_cd
    elif grade == 'C+':
        sum_grade += float_cd * 2.5
        sum_credit += float_cd
    elif grade == 'C0':
        sum_grade += float_cd * 2.0
        sum_credit += float_cd
    elif grade == 'D+':
        sum_grade += float_cd * 1.5
        sum_credit += float_cd
    elif grade == 'D0':
        sum_grade += float_cd * 1.0
        sum_credit += float_cd
    elif grade == 'F':
        sum_credit += float_cd
    else:
        continue

if sum_credit != 0:
    avg = sum_grade / sum_credit
    print(avg)
else:
    print(0)