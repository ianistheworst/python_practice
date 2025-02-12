import random
print('CONDITIONALS EXERCISES')

print('-' * 72)

random_number = random.randint(0, 1)
print(random_number)
if random_number == 1:
    print('Yes!')
else:
    print('No...')

print('-' * 72)

random_number = random.randint(0, 1)
print(random_number)
print('Yessir!' if random_number == 1 else 'No :(')

print('-' * 72)

weather = 'sunny'
if weather == 'sunny':
    print('It\'s a beautiful day')
elif weather == 'rainy':
    print('Grab your umbrella')
else:
    print('Let\'s stay inside')

print('-' * 72)

weather = 'sunny'
match weather:
    case 'sunny':
        print('It\'s a beautiful day!')
    case 'rainy':
        print('Grab your umbrelly')
    case _:
        print('Let\'s just stay inside')

print('-' * 72)

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)