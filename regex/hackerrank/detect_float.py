# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def isFloat(string):
    regex = re.compile('^[+-]?\d*\.\d*$')
    match = re.match(regex, string)
    if match:
        return True
    else:
        return False

num_tests = int(input())
tests = [input() for _ in range(num_tests)]

for test in tests:
    print(isFloat(test))
