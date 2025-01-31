my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

even_odd = []

for num in my_list:
    if num % 2 == 0:
        even_odd.append('even')
    else:
        even_odd.append('odd')

print(even_odd)