def number_range(number):
    num = int(number)
    if num < 0:
        print(f'{num} is less than 0')
    elif num > 100:
        print(f'{num} is greater than 100')
    elif 100 >= num >= 51:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is between 0 and 50')

number_range(25)
number_range(0)
number_range(50)
number_range(100)
number_range(101)
number_range(-1)