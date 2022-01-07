# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int,input().split())
A = defaultdict(list)
for i in range(n):
    A[input()].append(f'{i + 1}')
B = [input() for i in range(m)]

for word in B:
    if word in A:
        print(' '.join(A[word]))
    else:
        print(-1)