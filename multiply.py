def multiply(one, two):
    """
    Multiplies number one by number two
    """
    return (one * two)

num_one = float(input('Enter the first number\n'))
num_two = float(input('Enter the second number\n'))

print(f'{num_one} * {num_two} = ' + str(multiply(num_one, num_two)))