import re
message = 'Call me 555-555-5555 tomorrow, or at 123-123-1231 today'


# recall raw strings block the escape character and treat it literally.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = phoneNumRegex.search(message)
print(mo.group())
print(re.findall(phoneNumRegex, message))