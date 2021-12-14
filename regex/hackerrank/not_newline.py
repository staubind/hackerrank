import re

search_string = '123.456.abc.def'
regex = re.compile(r'((\w{3}\.){3}\w{3})')
print(re.findall(regex, search_string))