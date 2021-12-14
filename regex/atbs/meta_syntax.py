import re 
x = 'dan'
print(f'hello there, my friend {x}')

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print(f'Searching for pattern {pat}')
        print(re.findall(pat, phrase))
        print('\n')

# repetition syntax
test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd*'] # find an s, followed by 0 or more d's
test_pattern = ['sd+'] # find an s, followed by 1 or more d
test_pattern = ['sd?'] # find an s, followed by 0 or 1 d
test_pattern = ['sd{3}'] # find an s followed by EXACTLY 3 ds
test_pattern = ['sd{2,3}'] # find an s followed by 2 or three ds
# note that it, at least in python, will select the maximal number. i.e. sddd will return sddd, not sdd

test_pattern = ['s[sd]+'] # let me know where s is followed by one or more s's or one or more d's
multi_re_find(test_pattern, test_phrase)


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_pattern = ['[^!.?]+'] # caret means remove. so remove any of the following characters if they occur 1 or more times in a row
test_pattern = ['[a-z]+'] # find all instances of lowercase characters
test_pattern = ['[A-Z]+'] # find all instances of uppercase characters

multi_re_find(test_pattern, test_phrase)

test_pattern = [r'\d+'] # returns a sequence of digits - hence the escape character before the d
test_phrase = 'This is a string with numbers 12321 and a symbol #hashtag'

test_pattern = [r'\D+'] # returns a sequence of non-digits - hence the escape character before the d
test_pattern = [r'\s+'] # returns a sequence of space characters - need the backslash to escape and not treat it as the char s.
test_pattern = [r'\S+'] # returns a sequence of non-space characters - need the backslash to escape and not treat it as the char s.
test_pattern = [r'\w+'] # returns a sequence of alpha-numeric chars - need the backslash to escape and not treat it as the char s.
test_pattern = [r'\W+'] # returns a sequence of non-alpha-numeric chars - need the backslash to escape and not treat it as the char s.


multi_re_find(test_pattern, test_phrase)