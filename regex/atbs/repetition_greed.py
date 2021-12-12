import re

# ? match group 0 or 1 times
batRegex = re.compile(r'Bat(man|woman)?')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

# phone number example:
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# requires phone number to have an area code
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# try this for optional area codes:
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())

# can always use escape char to get a literal

# * to match zero or more times
batRegex = re.compile(r'Bat(man|woman)*')
mo = batRegex.search('The Adventures of Bat')
print(mo.group())
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

# + match one or more
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman!')
print(mo == None)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())
# as always, use \ for escape:
regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

# specific number of repetitions {int}
haRegex = re.compile(r'(ha){3}')
mo = haRegex.search('He said hahaha')
print(mo.group())
haRegex = re.compile(r'(ha){3,5}')
mo = haRegex.search('He said hahahahaha')
print(mo.group())


# another way to do the phone thing:
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )*){3}') # match three phone numbers in a row
mo = phoneRegex.search('123-123-1237, 555-555-5555, 123-1231')
# it seems that sub groups are only counted once per style of sub group and the last match is the one that is returned.
for i in range(3):
    print(mo.group(i))

# greedy
haRegex = re.compile(r'(ha){1,5}') # if you use 0,5 or just ,5 it returns an empty string. strange
mo = haRegex.search('He said hahahahahahahahahaha') # it only matches it one time, interestingly.
print(mo)

haRegex = re.compile(r'(ha){,}') # if you use 0,5 or just ,5 it returns an empty string. strange
mo = haRegex.search('He said hahahahahahahahahaha') # it only matches it one time, interestingly.
print(mo)

# # another way to do the phone thing:
# phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )*){3}') # match three phone numbers in a row
phoneRegex = re.compile(r'((\d{3}-)?\d{3}-\d{4}(, )?){3}')
mo = phoneRegex.search('123-123-1237, 555-555-5555, 123-1231')
# it seems that sub groups are only counted once per style of sub group and the last match is the one that is returned.
for i in range(3):
    print(mo.group(i))
print('------')
# to do non-greedy matches:
digitRegex = re.compile(r'(\d){3,5}?') # w/ the question mark it gets the minimum, rather than the maximum
mo = digitRegex.search('1234567890')
print(mo.group())