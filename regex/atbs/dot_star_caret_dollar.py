import re

# can also use ^ and $ to indicate it must start or end with the regex respectively
begins_with_hello_regex = re.compile(r'^Hello')
print(begins_with_hello_regex.findall('Hello there my friend, hello!'))
print(begins_with_hello_regex.findall('My friend, hello!'))
ends_with_hello_regex = re.compile(r'World$')
print(ends_with_hello_regex.findall('Hello World'))
print(ends_with_hello_regex.findall('World Hello'))
# starts and ends with ^ $ means mus tbe exactly
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.findall('34567898x75456789')) # even though it begins and ends with, it must do it with the same group

# wild card . char - any char except newline char
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in teh hat sat on the flat mat'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in teh hat sat on the flat mat'))


# dot-star to match anything - except new line.
some_text = 'First Name: Al Last Name: Sweigart'
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(re.findall(name_regex, some_text))
# dot-star is greedy.
# dot-start-questionMark is non-greedy.
serve = '<To serve humans> for dinner.>'
name_regex = re.compile(r'<(.*?)>')
print(re.findall(name_regex, serve))

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)
dot_star = re.compile(r'.*', re.DOTALL) # use re.DOTALL to have . include newlines.
print(re.findall(dot_star, prime))

# can also do case-insensitive
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) # use re.IGNORECASE to make it match all the same
print(re.findall(vowelRegex, 'Al, why is your programming book talk about RoboCop so much?'))