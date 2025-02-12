print('LISTS EXERCISES')
print('-' * 80)

def first(list):
    if list:
        return list[0]
    # else:
    #     return 'Empty list'

print(first(['Earth', 'Moon', 'Mars']))  # Earth 
print(first([]))  

print('-' * 80)

def last(list):
    if list:
        return list[-1]
    
print(last(['Earth', 'Moon', 'Mars']))  # Mars

print('-' * 80)

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.pop(0)
#energy.remove('fossil')
energy.append('geothermal')
print(energy)

print('-' * 80)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet)
print(alphabet_list)

print('-' * 80)

scores = [96, 47, 113, 89, 100, 102]
count = 0
for score in scores:
    if score >= 100:
        count += 1

high_scores = [score for score in scores if score >= 100]
print(len(high_scores))
print(count)

print('-' * 80)

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for words in vocabulary:
    for emotion in words:
        print(emotion)

print('-' * 80)

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

print('-' * 80)

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(isinstance(some_value1, list)) #this method is preferable
print(isinstance(some_value2, list))
print(type(some_value1) is list)
print(type(some_value2) is list)

print('-' * 80)

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(str, cities):
    return cities.count(str) > 0
    
print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

print('-' * 80)

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
full_pass = '-'.join(passcode)
print(full_pass)
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

print('-' * 80)

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']


# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)

grocery_list = list(reversed(grocery_list))
while len(grocery_list) > 0:
    print(grocery_list.pop())

print(grocery_list)

