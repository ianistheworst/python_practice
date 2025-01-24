pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))
# pets['Lizard'] = 'None'
# print(pets['Lizard'])
# pets['Lizard'] = '<silence>'
# print(pets['Lizard'])