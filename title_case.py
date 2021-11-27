import re
def solve(s):
    names = s.split(' ')
    title_names = []
    for name in names:
        if name[0].isdigit():
            title_names.append(name)
        else:
            title_names.append(name.title())
    return ' '.join(title_names)

print(solve('1 w 2 r 3g'))
print(solve('hello   world  lol'))
print(solve('132 456 Wq  M E'))

# need to respect spaces