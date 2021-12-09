# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
A = set(input().split())
n = int(input())
for i in range(n):
    cmd = input().split()[0]
    b = set(input().split())
    if cmd == 'intersection_update':
        A.intersection_update(b)
    if cmd == 'update':
        A.update(b)
    if cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(b)
    if cmd == 'difference_update':
        A.difference_update(b)
print(sum(map(int,A)))