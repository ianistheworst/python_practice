print('DICTIONARY EXERCISES')
def lines():
    print('-' * 72)

lines()

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}
print(car)

lines()

car['year'] = 2003
print(car)

lines()

car.pop('mileage', None) #Adding none has better error handling if key doesn't exist
#del car['mileage]
print(car)

lines()

print(car['color'])

lines()

print(car.items(), len(car))

lines()

student = {
    'id': 123,
    'grade': 'B',
}

print(student.keys())
print('name' in student)
print('grade' in student)

lines()

car = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'mileage': 80_000,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    }
}


print(car)

lines()

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003]
]
print(car)

lines()

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_values = []
half_values = [(value // 2) for value in numbers.values()]

# for value in numbers.values():
#     half_values.append((value // 2))

# for key in numbers:
#     half_values.append(int(numbers[key] / 2))
print(half_values)

lines()

for key, value in numbers.items():
    print(f'A {key} number is {value}')