def erase(ls):
    if len(ls) == 1:
        return '-'
    standard = len(ls)//3
    return erase(ls[:standard]) + ' ' * standard + erase(ls[2*standard:])
    
while True:
    try:
        N = int(input())
        Cantorian = '-' * (3**N)
        print(erase(Cantorian))
    except:
        break