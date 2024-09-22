dial = {'ABC' : 3, 'DEF' : 4, 'GHI' : 5, 'JKL' : 6, "MNO" : 7, "PQRS" : 8, "TUV" : 9, "WXYZ" : 10}
ch = input()
second = 0

for i in ch:
    for t, m in dial.items():
        if i in t:
            second += m
            
print(second)