my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

#create dict with keys as the string and the len of each string
#as the value. Only include values that are odd.

my_dict = {name: len(name) for name in my_set if len(name) % 2 != 0}
print(my_dict)