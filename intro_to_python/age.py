#calculates age from static variable
age = int(input('How old are you? \n'))
age_range = [10, 20, 30, 40]

for years in age_range:
    print(f'In {years} years you will be {age + years}')

#Alternatively

for years in range(10, 50, 10):
    print(f'In {years} years you will be {age + years}')

# print('in 10 years, you will be ' + str((age + 10)) + ' years old')
# print('in 20 years, you will be ' + str((age + 20)) + ' years old')
# print('in 30 years, you will be ' + str((age + 30)) + ' years old')

# print(f'this is using an f string, which you need to get better at remembering so 10 years, {age + 10} age')
