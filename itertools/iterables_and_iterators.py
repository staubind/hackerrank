# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
# n letters
# k indices
# find p(count=0|k chosen from n)
# need count of a, then can calculate directly.
len_n = int(input())
n = input().split()
k = int(input())

def prob_of_an_a(char_list, k):
    combos = list(combinations(char_list,k))
    count = 0
    for tupple in combos:
        if 'a' in tupple:
            count += 1
    return count/len(combos)
    
print(prob_of_an_a(n,k))