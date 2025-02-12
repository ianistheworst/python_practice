print('-' * 80)
print('FUNCTIONS EXERCISES')
print('-' * 80)

def multiply(num1, num2):
    print(num1 * num2)

multiply(12, 4)

print('-' * 80)

def bruce_eckel_quote():
    print('Python is executable pseudocode')

bruce_eckel_quote()

print('-' * 80)

def cite(string1, string2):
    print(f'{string1} said "{string2}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')

print('-' * 80)

def squared_number(num):
    return num**2

print(squared_number(3))

print('-' * 80)

def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    else:
        return 0
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

print('-' * 80)

#My Solution
ruby = 'Captain Ruby'
python = ruby.replace('Ruby', 'Python')
print(ruby)
print(python)

#Alternate Solutions
first_8 = 'Captain Ruby'[:8]
new_str = first_8 + 'Python'
print(new_str)      # Captain Python

all_words = 'Captain Ruby'.split(' ')
first_word = all_words[0]
new_str = first_word + ' Python'
print(new_str)      # Captain Python

print('-' * 80)

def greet(lang, lang2):
    match lang, lang2:
        case 'el', 'GR':
            return 'Γεια σου!'
        case 'nn', 'NO':
            return 'Hallo!'
        case 'ja', 'JA':
            return 'こんにちは'
        case 'en', 'US':
            return 'Well, yeehaw I\'m a Amurrican. Hurr durr guns. Trucks.'
        case 'en', 'GB':
            return "'ELLO GUVNAH CARE FOR A BISCUIT?"
        case 'en', 'AU':
            return 'Crikey, a wallaby bit my pecker off! Prawns! Kangaroo!'
        case 'fr', _:
            return "'Ello, vee have a false sense of superiority. Baguettes."
        case _:
            return 'Language not recognised, try again.'
    
print(greet('el', 'GR'))
# print(greet('nn'))
# print(greet('ja'))
# print(greet('ru'))

print('-' * 80)

def extract_language(locale):
    language = locale.split('_')
    alt_language = locale[:2]
    return alt_language
    #return language[0]


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

print('-' * 80)

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]
    #return locale[3:5]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

print('-' * 80)

def local_greet(locale):
    region = extract_region(locale)
    language = extract_language(locale)
    return greet(language, region)
    
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!