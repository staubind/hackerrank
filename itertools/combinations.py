# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

def print_combos(lst, num):
    for i in range(1, num + 1):
        for item in combinations(sorted(lst), i):
            print(''.join(item))

inpt = input().split()
string = list(inpt[0])
num = int(inpt[1])
print_combos(string,num)