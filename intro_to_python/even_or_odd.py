def even_or_odd(number):
    num = int(number)
    if num == 0:
        print('This is zero')
    elif (num % 2 == 0):
        print('even')
    else:
        print('pretty. odd.')

even_or_odd(5)
even_or_odd(4)
even_or_odd(0)