# Enter your code here. Read input from STDIN. Print output to STDOUT
# make combos of all function results from all lists
# find the modulo for each of them
# grab index of largest one

from itertools import product

sq = lambda x: x**2
line_one = input().split()
list_count = int(line_one[0])
mod = int(line_one[1])
lists = [list(map(int,input().split()[1:])) for i in range(list_count)]
    
def max_combo_mod(lists, func, mod):
    # make combos of all function results from all lists
    combos = list(product(*lists))
    maximum = max(combos, key=lambda x: sum(map(func,x)) % mod)
    return sum(map(func,maximum)) % mod
    
print(max_combo_mod(lists, sq, mod))