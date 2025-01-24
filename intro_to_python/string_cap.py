def string_caps(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(string_caps('ahoy'))
print(string_caps('ahoy you scurvy bint'))