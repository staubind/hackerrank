# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

def count_occurrences(iterable):
    groups = [list(k) for g, k in groupby(iterable)]
    print(groups)
    group_strings = map(lambda a: f'({len(a)}, {a[0]})', groups)
    return ' '.join(group_strings)

print(count_occurrences('112233'))