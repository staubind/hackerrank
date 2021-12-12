import re

# character classes
lyrics = '''
12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree
'''

xmasRegex = re.compile(r'\d+ \w+')
print(re.findall(xmasRegex, lyrics))

# to create your own character classes:
regex_object = re.compile(r'[aeiouAEIOU]') # same as a regular expression using r'(a|e|i|o|u)'
a_thru_f = re.compile(r'[a-fA-F]')
regex_object = re.compile(r'[aeiouAEIOU]{2}') # same as a regular expression using r'(a|e|i|o|u){2}'
print(regex_object.findall('Robocop eats baby food.'))

# use a ^ to make a "negative" character class:
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food.'))