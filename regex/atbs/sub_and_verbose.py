import re

names_regex = re.compile(r'Agent \w+')
text = 'Agent Alice gave the secret documents to Agent Bob.'
matches = names_regex.findall(text)
print(matches)

# find and substitute and return the new string
new_string = names_regex.sub('REDACTED', text)
print(new_string)

# Or...
names_regex = re.compile(r'Agent (\w)\w*')
new_string = names_regex.sub(r'Agent \1****', text) # use the text from group 1's match.
print(new_string)

# VERBOSE
re.compile(
    r'''
    (\d\d\d)|    # area code
    (\(\d\d\d\) )# -or- area code with parens and no dash
    -
    \d\d\d    # first 3 digits
    -
    \d\d\d\d  # final 4 digits
    \sx\d{2,4}# extension, like x1234
    ''', 
    re.IGNORECASE | re.DOTALL | re.VERBOSE) # use pipe in regex to combine all of the options you want.