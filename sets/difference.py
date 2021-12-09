# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
a = set(input().split())
input()
b = set(input().split())
print(len(a.difference(b)))