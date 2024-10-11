while True:
    n = int(input())
    if n == -1:
        break
    else:
        divisor_sum = 0
        divisor = []
        for i in range(1, n):
            if n % i == 0:
                divisor_sum += i
                divisor.append(i)
        if divisor_sum == n:
            result = ' + '.join(map(str, divisor))
            print(f'{n} = {result}')
        else:
            print(f'{n} is NOT perfect.')