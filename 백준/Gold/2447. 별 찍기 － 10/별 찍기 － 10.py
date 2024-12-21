def draw_star(n):
    if n == 3:
        return ['***', '* *', '***']
    star = draw_star(n//3)
    result = []
    
    for st in star:
        result.append(st * 3)
    for st in star:
        result.append(st + ' ' * (n//3) + st)
    for st in star:
        result.append(st * 3)
    
    return result

N = int(input())
print('\n'.join(draw_star(N)))