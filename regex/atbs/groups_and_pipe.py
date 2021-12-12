import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
#print(mo.group())
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # parentheses mark out groups
mo = phoneNumRegex.search('My number is 415-555-4242')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group()) # print whole match

# so what if the text has parentheses? - raw strings w/ an escape character
phoneNumRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415)-555-4242')
print(mo.group())

# pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # pipe is or. match one of the suffixes in this group
# you can also use + at the end of the group to match multiple
mo = batRegex.search('Batmobileman lost a wheel')
print(mo.group())
#mo = batRegex.search('Batmotorcycle lost a wheel')
#print(mo.group()) # returns an error because motorcycle wasn't one of the potential match objects, so no group exists
# to print out the suffix only:
print(mo.group(1))
