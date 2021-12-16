#12-45-7810 -> false
#12-34-56-78 -> true
#12345678 -> true
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"	# Do not delete 'r'.

import re
print(re.findall(Regex_Pattern, '12345678')) # should return false