print('STRINGS EXERCISES')
print('-' * 80)

print(len("These aren't the droids you're looking for."))

print('-' * 80)

print('confetti floating everywhere'.upper())

print('-' * 80)

name = 'Roger'

print(name.casefold() == 'RoGer'.casefold())
print(name.casefold() == 'DAVE'.casefold())

print('-' * 80)

song = 'A pirate I was meant to be! \nTrim the sails and roam the sea!'
#or
song2 = '''A pirate etc etc
Trim the etc etc'''
print(song)
print(song2)

print('-' * 80)

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)
print(char_sequence.find('x'))
print(char_sequence.rfind('x'))


print('-' * 80)

def is_empty(str):
    #return len(str) == 0
    #return len(str) == 0
    return not str
    
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

print('-' * 80)

def is_empty_or_blank(str):
    #return not str or str.isspace()
    #return not str.strip(' ')
    return False if str.strip(' ') else True

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

print('-' * 80)

print('launch school tech & talk'.title())

print('-' * 80)


def starts_with(str, pre):
    return str.startswith(pre)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

print('-' * 80)

def count_substrings(str, sub):
    return str.count(sub)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0