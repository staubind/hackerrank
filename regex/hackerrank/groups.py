Regex_Pattern = r'(?:ok){3}!'	# Do not delete 'r'.

import re

print(re.findall(Regex_Pattern, 'okokok! cya'))