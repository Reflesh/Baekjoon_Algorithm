num, square, div = map(int, input().split())

def sol(num, square):
    if square == 1:
        return num % div
    else:
        tmp = sol(num, square // 2)
        if square % 2 == 0:
            return (tmp * tmp) % div
        else:
            return (tmp * tmp * num) % div
    
print(sol(num, square))