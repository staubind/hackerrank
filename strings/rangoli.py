def make_line(start, end):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    line = ''
    for i in range(start,end):
        if i == start:
            line += alphabet[i]
        else:
            line = '-'.join([alphabet[i],line,alphabet[i]])
    return line.center(4*end-3, '-')

def print_rangoli(size):
    # your code goes here
    lines = []
    for i in range(size):
        lines.append(make_line(i, size))
    print('\n'.join([*lines[::-1],*lines[1:]]))

print_rangoli(26)
