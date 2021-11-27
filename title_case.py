import re

def solve(s):

    # Capitalize in Python - HackerRank Solution START
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

print(solve('1 w 2 r 3g'))
print(solve('hello   world  lol'))
print(solve('132 456 Wq  M E'))
print(solve('hihi ihihihi fabulos, 12abc'))
# need to respect spaces