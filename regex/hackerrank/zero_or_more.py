Regex_Pattern = r'^(\d{2,}[a-z]*){1}([A-Z]*)$'	# Do not delete 'r'.
#13123sc132123
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())