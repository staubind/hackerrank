# Enter your code here. Read input from STDIN. Print output to STDOUT

# will want to use an ordered dict
from collections import Counter, OrderedDict
# and perhaps a counter
n = int(input())

words = [input() for i in range(n)]
ordered_counter = OrderedDict()

for word in words: 
    ordered_counter[word] = ordered_counter.setdefault(word, 0) + 1


print(len(ordered_counter.keys()))
print(' '.join(map(str, ordered_counter.values())))