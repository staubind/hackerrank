# via Jose's Django class

import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other!'

match = re.search('term1', text)

print(type(match))
print('\n')
print(match.start())

split_term = '@'

email = 'user@gmail.com'

match = re.split(split_term, email)

print(match)



print(re.findall('match', 'test phrase match matchin middle'))
