import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(results:= re.findall(phoneRegex, '123-123-1231 555-555-5555'))
print('a result is: ' + results[0])