t = int(input())

for i in range(t):
    cent = int(input())
    quarter = cent // 25
    cent -= quarter * 25
    
    dime = cent // 10
    cent -= dime * 10
    
    nickel = cent // 5
    cent -= nickel * 5
    
    penny = cent
    
    print(quarter, dime, nickel, penny, end = " ")
    print()