Regex_Pattern = r"(?<![aeiouAEOIU])[\w\W]"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))