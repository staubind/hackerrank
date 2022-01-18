# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

num_cases = int(input())
tests = [input().strip() for i in range(num_cases)]

for i in range(num_cases):
    try:
        re.compile(tests[i])
    except:
        print(False)
    else: 
        print(True)