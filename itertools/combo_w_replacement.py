# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

def combo_replace(iterable, number):
    for elem in combinations_with_replacement(sorted(iterable), number):
        print(''.join(elem))

    
inpt = input().split()
string = inpt[0]
num = int(inpt[1])
combo_replace(string, num)