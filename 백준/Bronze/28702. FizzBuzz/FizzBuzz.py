for i in range(3, 0, -1):
    num = input()
    if num not in ['Fizz', 'Buzz', 'FizzBuzz']:
        result = int(num) + i
        
if result % 15 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)