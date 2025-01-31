# Looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

for values in my_dict.values():
    print(values)

for items in my_dict.items():
    print(items)

for key, value in my_dict.items():
    print(f'{key} = {value}')