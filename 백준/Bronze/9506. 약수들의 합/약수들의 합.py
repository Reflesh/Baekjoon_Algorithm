while True:
    n = int(input())
    if n == -1:
        break
    else:
        divisor = []
        for i in range(1, n):
            if n % i == 0:
                divisor.append(i)
        if sum(divisor) == n:
            result = ' + '.join(map(str, divisor))
            print(f'{n} = {result}')
        else:
            print(f'{n} is NOT perfect.')