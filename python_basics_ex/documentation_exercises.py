from datetime import datetime

print('-' * 80)
print('DOCUMENTATION EXERCISES')

print('-' * 80)

string = 'abcdefg'
newstring = string.rjust(10)
print(string)
print(newstring)

print('-' * 80)

list1 = ['1', '2', '3']
print('2' in list1)
print(list1.index('2'))

print('-' * 80)

name = "Victor"
profession = "programmer"
print('Hello, {0}, you are a {1}'.format(name, profession))

print('-' * 80)

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

print('-' * 80)

print((4 * 5) + ((3**2) / 10))

print('-' * 80)

now = datetime.now()
print(now)

print('-' * 80)

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')

print('-' * 80)
