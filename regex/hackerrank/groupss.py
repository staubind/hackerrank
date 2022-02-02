# choices for me:

# 1
# 12
# 13
# 17

#how learn
# 4
# 1/2
# 1/2

# team stuff
# 3 demonstrations of trust
# 6 enganged listening and ocmmunication
# 8 social relationships
# 1 clear accountability

# stuff 1/12/13/17
# complexity reduction
# ingenuity
# motivation
# gap detection

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_repeats(string):
    regex = re.compile(r'([a-zA-Z0-9])\1+')
    match = re.search(regex, string)
    if match:
        return(match.group(1))
    else:
        return -1
        
inpt = input()
print(find_repeats(inpt))

        
print(find_repeats('hello theree'))