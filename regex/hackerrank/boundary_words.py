Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

import re

print(re.findall(Regex_Pattern, 'Found any match?'))