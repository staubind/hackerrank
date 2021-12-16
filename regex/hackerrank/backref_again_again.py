#ab #1?AZa$ab #1?AZa$
Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeoiuAEOIU])(\S)\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.

import re
print(re.findall(Regex_Pattern, 'ab #1?AZa$ab #1?AZa$'))
print(str(bool(re.search(Regex_Pattern, 'ab #1?AZa$ab #1?AZa$'))).lower())