# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def string_permutations(lst, k):
    for element in permutations(sorted(lst), k):
        print(''.join(element))
    

strings = list('ABCD')
perm_length = 3

string_permutations(strings, perm_length)