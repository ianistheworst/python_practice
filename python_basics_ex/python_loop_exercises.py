print('PYTHON BASICS- LOOP EXERCISES')

print('-' * 80)

for num in range(0, 15, 2):
    print(num)

print('-' * 80)

for i in range(10, 0, -1):
    print(i)
print('Launch!')

print('-' * 80)

greeting = 'Aloha!'
for i in range(1, 4):
    print(greeting)

print('-' * 80)

for i in range(1, 101):
    sum = i * 2
    print(sum)

print('-' * 80)

lst = [1, 3, 7, 15]
index = 0
while index < len(lst):
    print(lst[index])
    index += 1

print('-' * 80)

friends = ['Sarah', 'John', 'Hannah', 'Dave']
for name in friends:
    print(f'Hello, {name}!')

print('-' * 80)

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    else:
        print(len(city))

print('-' * 80)

while True:
    print("and on")
    break

print('-' * 80)

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
index = 0
fish_two = []
for fish in fish_list:
    if fish == 'Bruce':
        break
    fish_two.append(fish)
print(fish_two)
#my OG solution. The assignment said to log each fish so I interpreted it
#as making a new list. Still the correct answer though,
while index < len(fish_list):
    if fish_list[index] == 'Bruce':
        break
    print(fish_list[index])
    index += 1

print('-' * 80)

while True:
    print('Should I stop looping?')
    answer = input().casefold()
    if answer == 'yes':
        break