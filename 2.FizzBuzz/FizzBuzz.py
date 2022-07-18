
number = range(0,100)
for i in number:
    if i == 0:
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i != 0:
        print(i)
