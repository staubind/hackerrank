# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
meth_val = [input().split() for i in range(n)]
d = deque()

for operation in meth_val:
    meth = operation[0]
    if meth == 'append':
        d.append(operation[1])
    elif meth == 'pop':
        d.pop()
    elif meth == 'popleft':
        d.popleft()
    else:
        d.appendleft(operation[1])
        
print(' '.join(d))