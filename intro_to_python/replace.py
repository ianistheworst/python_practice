info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
print(parts)
result = '+'.join(parts)
print(result)
print(info)

#print(info.replace(':', '+'))

